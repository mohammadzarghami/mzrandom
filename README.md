# MZRandom: A Comprehensive Random Number Generator Library

MZRandom is a high-entropy, highly customizable random number generator library for Python. It combines multiple entropy sources to ensure unpredictability and supports various pseudorandom number generator (PRNG) algorithms. With a robust API, MZRandom provides a wide range of functionalities for generating random numbers, shuffling sequences, and sampling from statistical distributions.

---

## Features

- **High Entropy**: Utilizes multiple entropy sources such as system time, OS state, garbage collection, and platform information to ensure robust randomness.
- **Customizable PRNG Algorithms**: Supports three advanced PRNG algorithms:
  - **Xorshift1024**: Fast and efficient for general-purpose use.
  - **PCG64**: A high-quality PRNG with excellent statistical properties.
  - **ChaCha20**: A cryptographic PRNG for high-security applications.
- **Thread-Safe Operations**: Ensures safe usage in multi-threaded environments with locking mechanisms.
- **Comprehensive API**:
  - Generate random floats, integers, and sequences.
  - Shuffle lists and sample from populations.
  - Generate random numbers from various statistical distributions (e.g., normal, gamma, exponential).
- **Extensible**: Add custom entropy sources or PRNG algorithms as needed.

---

## Installation

You can install MZRandom using `pip`:

```bash
pip install mzrandom
```

---

## Quick Start

### Basic Usage

```python
from mzrandom import MZRandom

# Initialize with the PCG64 algorithm
cr = MZRandom(prng_algorithm="pcg64")

# Generate a random float between 0.0 and 1.0
print(cr.random())

# Generate a random integer between 1 and 100
print(cr.randint(1, 100))

# Shuffle a list in place
my_list = [1, 2, 3, 4, 5]
cr.shuffle(my_list)
print(my_list)

# Sample 2 unique elements from a population
print(cr.sample([1, 2, 3, 4, 5], 2))
```

### Advanced Usage

```python
# Generate a random number from a normal distribution
print(cr.normalvariate(mu=0, sigma=1))

# Generate a random number from a gamma distribution
print(cr.gammavariate(alpha=1, beta=2))

# Generate a random number from a triangular distribution
print(cr.triangular(low=0, high=10, mode=5))
```

---

## API Reference

### Initialization

```python
MZRandom(entropy_sources=None, prng_algorithm="xorshift1024")
```

- **`entropy_sources`**: A list of callable functions that generate entropy. If not provided, the default entropy sources are used.
- **`prng_algorithm`**: The pseudorandom number generator algorithm to use. Options include:
  - `"xorshift1024"` (default)
  - `"pcg64"`
  - `"chacha20"`

### Key Methods

#### Random Number Generation
- **`random()`**: Returns a random float in the range [0.0, 1.0).
- **`randint(a, b)`**: Returns a random integer between `a` and `b` (inclusive).
- **`randrange(start, stop=None, step=1)`**: Returns a randomly selected element from `range(start, stop, step)`.

#### Sequence Operations
- **`choice(seq)`**: Returns a random element from a non-empty sequence.
- **`choices(population, weights=None, cum_weights=None, k=1)`**: Returns a `k`-sized list of elements chosen from `population` with replacement.
- **`shuffle(x)`**: Shuffles the sequence `x` in place.
- **`sample(population, k)`**: Returns a `k`-length list of unique elements chosen from `population`.

#### Statistical Distributions
- **`normalvariate(mu, sigma)`**: Returns a random float from a normal distribution with mean `mu` and standard deviation `sigma`.
- **`gammavariate(alpha, beta)`**: Returns a random float from a gamma distribution with shape `alpha` and scale `beta`.
- **`triangular(low, high, mode)`**: Returns a random float from a triangular distribution with lower bound `low`, upper bound `high`, and mode `mode`.
- **`expovariate(lambd)`**: Returns a random float from an exponential distribution with rate `lambd`.
- **`betavariate(alpha, beta)`**: Returns a random float from a beta distribution with parameters `alpha` and `beta`.
- **`lognormvariate(mu, sigma)`**: Returns a random float from a log-normal distribution with parameters `mu` and `sigma`.

#### State Management
- **`seed(a=None)`**: Seeds the random number generator. If `a` is `None`, the generator is seeded using entropy sources.
- **`getstate()`**: Returns the current internal state of the generator.
- **`setstate(state)`**: Restores the generator's internal state.

---

## Customization

### Adding Custom Entropy Sources

You can add custom entropy sources by passing a list of callable functions to the `entropy_sources` parameter during initialization. Each function should return a value that can be converted to bytes or a string.

```python
def custom_entropy():
    return "my_custom_entropy_data"

cr = MZRandom(entropy_sources=[custom_entropy, ...])
```

### Implementing a Custom PRNG Algorithm

To implement a custom PRNG algorithm, subclass `MZRandom` and override the `_initialize_prng` and `_update_prng_state` methods.

---

## Contributing

Contributions are welcome! If you'd like to contribute to MZRandom, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a detailed description of your changes.

---

## License

MZRandom is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

---

## Support

For questions, issues, or feature requests, please open an issue on the [GitHub repository](https://github.com/yourusername/mzrandom).

---

# MZRandom: کتابخانه‌ای جامع برای تولید اعداد تصادفی

MZRandom یک کتابخانه پیشرفته و قابل تنظیم برای تولید اعداد تصادفی در پایتون است. این کتابخانه با استفاده از منابع متعدد انتروپی و الگوریتم‌های پیشرفته، اعداد تصادفی با کیفیت بالا و غیرقابل پیش‌بینی تولید می‌کند.

---

## ویژگی‌ها

- **انتروپی بالا**: از منابع مختلفی مانند زمان سیستم، وضعیت OS، و اطلاعات حافظه برای تولید اعداد تصادفی استفاده می‌کند.
- **الگوریتم‌های قابل تنظیم**: از سه الگوریتم پیشرفته پشتیبانی می‌کند:
  - **Xorshift1024**: سریع و کارآمد برای استفاده عمومی.
  - **PCG64**: یک الگوریتم با کیفیت بالا و خواص آماری عالی.
  - **ChaCha20**: یک الگوریتم رمزنگاری برای کاربردهای امنیتی.
- **عملیات ایمن در محیط‌های چند رشته‌ای**: با استفاده از مکانیزم‌های قفل‌گذاری، عملیات در محیط‌های چند رشته‌ای ایمن است.
- **API جامع**:
  - تولید اعداد تصادفی اعشاری، صحیح و دنباله‌ها.
  - جابجایی لیست‌ها و نمونه‌گیری از جمعیت‌ها.
  - تولید اعداد تصادفی از توزیع‌های آماری مختلف (مانند نرمال، گاما، نمایی).
- **قابل توسعه**: امکان افزودن منابع انتروپی یا الگوریتم‌های جدید.

---

## نصب

برای نصب MZRandom از `pip` استفاده کنید:

```bash
pip install mzrandom
```

---

## شروع سریع

### مثال ساده

```python
from mzrandom import MZRandom

# مقداردهی اولیه با الگوریتم PCG64
cr = MZRandom(prng_algorithm="pcg64")

# تولید یک عدد اعشاری تصادفی بین 0.0 و 1.0
print(cr.random())

# تولید یک عدد صحیح تصادفی بین 1 و 100
print(cr.randint(1, 100))

# جابجایی یک لیست به صورت درجا
my_list = [1, 2, 3, 4, 5]
cr.shuffle(my_list)
print(my_list)

# نمونه‌گیری ۲ عنصر منحصر به فرد از یک جمعیت
print(cr.sample([1, 2, 3, 4, 5], 2))
```

### مثال پیشرفته

```python
# تولید یک عدد تصادفی از توزیع نرمال
print(cr.normalvariate(mu=0, sigma=1))

# تولید یک عدد تصادفی از توزیع گاما
print(cr.gammavariate(alpha=1, beta=2))

# تولید یک عدد تصادفی از توزیع مثلثی
print(cr.triangular(low=0, high=10, mode=5))
```

---

## راهنمای API

### مقداردهی اولیه

```python
MZRandom(entropy_sources=None, prng_algorithm="xorshift1024")
```

- **`entropy_sources`**: لیستی از توابع قابل فراخوانی که انتروپی تولید می‌کنند. اگر ارائه نشود، از منابع پیش‌فرض استفاده می‌شود.
- **`prng_algorithm`**: الگوریتم تولید اعداد تصادفی. گزینه‌ها شامل:
  - `"xorshift1024"` (پیش‌فرض)
  - `"pcg64"`
  - `"chacha20"`

### متدهای کلیدی

#### تولید اعداد تصادفی
- **`random()`**: یک عدد اعشاری تصادفی در بازه [0.0, 1.0) برمی‌گرداند.
- **`randint(a, b)`**: یک عدد صحیح تصادفی بین `a` و `b` (شامل هر دو) برمی‌گرداند.
- **`randrange(start, stop=None, step=1)`**: یک عنصر تصادفی از `range(start, stop, step)` برمی‌گرداند.

#### عملیات روی دنباله‌ها
- **`choice(seq)`**: یک عنصر تصادفی از یک دنباله غیرخالی برمی‌گرداند.
- **`choices(population, weights=None, cum_weights=None, k=1)`**: یک لیست به اندازه `k` از عناصر انتخاب شده از `population` با جایگزینی برمی‌گرداند.
- **`shuffle(x)`**: دنباله `x` را به صورت درجا جابجا می‌کند.
- **`sample(population, k)`**: یک لیست به اندازه `k` از عناصر منحصر به فرد از `population` برمی‌گرداند.

#### توزیع‌های آماری
- **`normalvariate(mu, sigma)`**: یک عدد تصادفی از توزیع نرمال با میانگین `mu` و انحراف معیار `sigma` برمی‌گرداند.
- **`gammavariate(alpha, beta)`**: یک عدد تصادفی از توزیع گاما با پارامترهای `alpha` و `beta` برمی‌گرداند.
- **`triangular(low, high, mode)`**: یک عدد تصادفی از توزیع مثلثی با کران پایین `low`، کران بالا `high` و مد `mode` برمی‌گرداند.
- **`expovariate(lambd)`**: یک عدد تصادفی از توزیع نمایی با نرخ `lambd` برمی‌گرداند.
- **`betavariate(alpha, beta)`**: یک عدد تصادفی از توزیع بتا با پارامترهای `alpha` و `beta` برمی‌گرداند.
- **`lognormvariate(mu, sigma)`**: یک عدد تصادفی از توزیع لگ‌نرمال با پارامترهای `mu` و `sigma` برمی‌گرداند.

#### مدیریت وضعیت
- **`seed(a=None)`**: مولد اعداد تصادفی را مقداردهی اولیه می‌کند. اگر `a` برابر `None` باشد، از منابع انتروپی استفاده می‌شود.
- **`getstate()`**: وضعیت فعلی مولد را برمی‌گرداند.
- **`setstate(state)`**: وضعیت مولد را بازیابی می‌کند.

---

## توسعه

### افزودن منابع انتروپی سفارشی

با ارسال لیستی از توابع قابل فراخوانی به پارامتر `entropy_sources`، می‌توانید منابع انتروپی سفارشی اضافه کنید.

```python
def custom_entropy():
    return "داده‌های انتروپی سفارشی"

cr = MZRandom(entropy_sources=[custom_entropy, ...])
```

### پیاده‌سازی الگوریتم‌های سفارشی

برای پیاده‌سازی الگوریتم‌های سفارشی، کلاس `MZRandom` را ارث‌بری کرده و متدهای `_initialize_prng` و `_update_prng_state` را بازنویسی کنید.

---

## مشارکت

مشارکت‌ها مورد استقبال هستند! برای مشارکت در توسعه MZRandom، مراحل زیر را دنبال کنید:

1. مخزن را Fork کنید.
2. یک شاخه جدید برای ویژگی یا رفع اشکال ایجاد کنید.
3. یک Pull Request با توضیحات کامل از تغییرات ارسال کنید.

---

## مجوز

MZRandom تحت مجوز **MIT** ارائه شده است. برای اطلاعات بیشتر، فایل [LICENSE](LICENSE) را مطالعه کنید.

---

## پشتیبانی

برای سوالات، مشکلات یا درخواست ویژگی‌ها، لطفاً یک Issue در [مخزن GitHub](https://github.com/yourusername/mzrandom) باز کنید.

---
