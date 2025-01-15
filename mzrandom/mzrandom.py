import time
import os
import sys
import hashlib
import gc
import platform
import threading
from typing import List, Any, Callable
import random as stdlib_random
import psutil

class MZRandom:
    """
    A high-entropy and highly unpredictable random number generator library.
    """
    def __init__(self, entropy_sources: List[Callable] = None, prng_algorithm: str = "xorshift1024"):
        self._seed_lock = threading.Lock()
        self._entropy_sources = entropy_sources or self._get_default_entropy_sources()
        self._prng_algorithm = prng_algorithm
        self._prng_state = None
        self._seed = self._get_initial_seed()
        self._update_prng_state(self._seed)
        self._prng_function = self._initialize_prng()

    def _get_default_entropy_sources(self) -> List[Callable]:
        """Return the default list of entropy sources."""
        return [
            self._get_time_entropy,
            self._get_os_entropy,
            self._get_system_stats_entropy,
            self._get_gc_entropy,
            self._get_platform_entropy,
        ]

    def _get_initial_seed(self) -> int:
        """Gather initial entropy and generate a seed."""
        combined_entropy = bytearray()
        for source in self._entropy_sources:
            try:
                entropy = source()
                if isinstance(entropy, str):
                    combined_entropy.extend(entropy.encode('utf-8'))
                elif isinstance(entropy, bytes):
                    combined_entropy.extend(entropy)
                elif isinstance(entropy, (int, float, tuple, list, dict)):
                    combined_entropy.extend(str(entropy).encode('utf-8'))
            except Exception as e:
                print(f"Error collecting entropy from {source.__name__}: {e}")
        return int(hashlib.sha512(combined_entropy).hexdigest(), 16)

    def _update_prng_state(self, seed: int):
        """Update the PRNG state using the seed."""
        if self._prng_algorithm == "xorshift1024":
            self._prng_state = [seed + i for i in range(32)]
        elif self._prng_algorithm == "pcg64":
            # Initialize both state and inc based on the seed
            self._prng_state = (seed, seed ^ 0xdeadbeef)
        elif self._prng_algorithm == "chacha20":
            self._prng_state = (seed.to_bytes(32, 'little'), [0] * 16) # Not a proper ChaCha20 init
        else:
            raise ValueError(f"Unknown PRNG algorithm: {self._prng_algorithm}")

    def _initialize_prng(self) -> Callable:
        """Create an instance of the PRNG."""
        if self._prng_algorithm == "xorshift1024":
            return self._xorshift1024
        elif self._prng_algorithm == "pcg64":
            return self._pcg64
        elif self._prng_algorithm == "chacha20":
            return self._chacha20
        raise ValueError(f"Unknown PRNG algorithm: {self._prng_algorithm}")

    def _mix_entropy(self, new_entropy: Any):
        """Mix new entropy into the current state."""
        combined = str(self._seed ^ hash(new_entropy)).encode('utf-8')
        hashed = hashlib.blake2b(combined).hexdigest()
        self._seed = int(hashed, 16)
        self._update_prng_state(self._seed)

    def _get_time_entropy(self) -> str:
        return str(time.time_ns())

    def _get_os_entropy(self) -> bytes:
        return os.urandom(64)

    def _get_system_stats_entropy(self) -> str:
     entropy = str(os.times())
     if hasattr(sys, 'getloadavg'):
        entropy += str(sys.getloadavg())
     elif os.name == 'nt':  # برای سیستم عامل ویندوز
        entropy += str(psutil.cpu_percent())
     return entropy

    def _get_gc_entropy(self) -> str:
        return str(gc.get_stats())

    def _get_platform_entropy(self) -> str:
        return str(platform.uname())

    def random(self) -> float:
        """Return a random float between 0.0 and 1.0."""
        with self._seed_lock:
            return self._prng_function()

    def _xorshift1024(self) -> float:
        """Xorshift1024 algorithm implementation."""
        x = self._prng_state
        t = x[0]
        s = x[13]
        b = x[10]
        c = x[23]
        x[0] = s
        x[10] = c
        x[13] = t
        x[23] = b
        t ^= t << 23
        t ^= t >> 18
        t ^= s ^ (s >> 5)
        self._prng_state = x[1:] + [t]
        return t / (2**64)

    def _pcg64(self) -> float:
        """PCG64 algorithm implementation."""
        state, inc = self._prng_state
        self._prng_state = (state * 6364136223846793005 + (inc | 1), inc)
        output_xor = state ^ (state >> 22)
        output_rotr = output_xor >> 61 ^ output_xor

        # Ensure output_rotr is treated as an unsigned 64-bit integer
        output_64bit = output_rotr & 0xFFFFFFFFFFFFFFFF

        return output_64bit / float(2**64)

    def _chacha20(self) -> float:
        """ChaCha20 algorithm implementation (simplified)."""
        key, counter = self._prng_state
        self._prng_state = (key, [(c + 1) % (2**32) for c in counter]) # Increment counter (simplified)
        # This is a placeholder; a full ChaCha20 implementation is complex
        return hash((key, tuple(counter))) / (2**128)

    def seed(self, a=None):
        """Seed the random number generator."""
        with self._seed_lock:
            if a is None:
                self._seed = self._get_initial_seed()
            else:
                self._seed = hash(a)
            self._update_prng_state(self._seed)

    def getstate(self):
        """Return the current internal state of the generator."""
        return (self._prng_algorithm, self._prng_state)

    def setstate(self, state):
        """Set the internal state of the generator."""
        algorithm, prng_state = state
        if algorithm != self._prng_algorithm:
            raise ValueError("State is for a different PRNG algorithm")
        self._prng_state = prng_state
        self._prng_function = self._initialize_prng()

    def randint(self, a: int, b: int) -> int:
        """Return a random integer N such that a <= N <= b."""
        return int(self.random() * (b - a + 1)) + a

    def randrange(self, start: int, stop: int = None, step: int = 1) -> int:
        """Return a randomly selected element from range(start, stop, step)."""
        if stop is None:
            stop = start
            start = 0
        if step > 0:
            n = (stop - start + step - 1) // step
        elif step < 0:
            n = (start - stop + (-step) - 1) // (-step)
        else:
            raise ValueError("step must not be zero")
        if n <= 0:
            raise ValueError("range contains no elements")
        return start + self.randint(0, n - 1) * step

    def choice(self, seq):
        """Return a random element from a non-empty sequence."""
        return seq[self.randrange(len(seq))]

    def choices(self, population, weights=None, cum_weights=None, k=1):
        """Return a k-sized list of elements chosen from the population with replacement."""
        if cum_weights is None:
            if weights is None:
                return [self.choice(population) for _ in range(k)]
            cum_weights = list(stdlib_random.accumulate(weights))
        if len(cum_weights) != len(population):
            raise ValueError("The number of weights does not match the population")
        n = len(cum_weights)
        return [population[stdlib_random.bisect_right(cum_weights, self.random() * cum_weights[-1])] for _ in range(k)]

    def shuffle(self, x: list):
        """Shuffle a list in place."""
        for i in reversed(range(1, len(x))):
            j = int(self.random() * (i + 1))
            x[i], x[j] = x[j], x[i]

    def sample(self, population, k):
        """Return a k-length list of unique elements chosen from the population."""
        n = len(population)
        if not 0 <= k <= n:
            raise ValueError("Sample larger than population or is negative")
        result = list(population)
        self.shuffle(result)
        return result[:k]

    def uniform(self, a: float, b: float) -> float:
        """Return a random floating point number N such that a <= N <= b."""
        return a + (b - a) * self.random()

    def normalvariate(self, mu: float, sigma: float) -> float:
        """Normal distribution."""
        return stdlib_random.normalvariate(mu, sigma)

    def vonmisesvariate(self, mu: float, kappa: float) -> float:
        """Von Mises distribution."""
        return stdlib_random.vonmisesvariate(mu, kappa)

    def gammavariate(self, alpha: float, beta: float) -> float:
        """Gamma distribution."""
        return stdlib_random.gammavariate(alpha, beta)

    def betavariate(self, alpha: float, beta: float) -> float:
        """Beta distribution."""
        return stdlib_random.betavariate(alpha, beta)

    def expovariate(self, lambd: float) -> float:
        """Exponential distribution."""
        return stdlib_random.expovariate(lambd)

    def lognormvariate(self, mu: float, sigma: float) -> float:
        """Log-normal distribution."""
        return stdlib_random.lognormvariate(mu, sigma)

    def triangular(self, low: float, high: float, mode: float) -> float:
        """Triangular distribution."""
        return stdlib_random.triangular(low, high, mode)

    def weibullvariate(self, alpha: float, beta: float) -> float:
        """Weibull distribution."""
        return stdlib_random.weibullvariate(alpha, beta)

    def paretovariate(self, alpha: float) -> float:
        """Pareto distribution."""
        return stdlib_random.paretovariate(alpha)

    def gauss(self, mu: float, sigma: float) -> float:
        """Gaussian distribution."""
        return stdlib_random.gauss(mu, sigma)
