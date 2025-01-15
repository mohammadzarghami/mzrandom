# MZRandom: A Comprehensive Random Number Library

MZRandom is a versatile and feature-rich random number library designed for Python. It enhances randomness using multiple entropy sources, supports customizable PRNG algorithms, and provides a robust API for statistical and utility-based random operations.

---

## Features

- **High Entropy**: Combines various entropy sources such as system time, OS state, and garbage collection.
- **Customizable PRNG Algorithms**: Supports Xorshift1024, PCG64, and ChaCha20.
- **Wide Functionality**:
  - Random floats, integers, and sequences
  - Shuffling and sampling
  - Statistical distributions (normal, gamma, etc.)
- **Thread-Safe**: Ensures safe operations in multi-threaded environments.

---

## Installation

```bash
pip install mzrandom
```

---

## Usage

### Basic Example

```python
from mzrandom import MZRandom

cr = MZRandom(prng_algorithm="pcg64")

# Generate random numbers
print(cr.random())  # Float between 0.0 and 1.0
print(cr.randint(1, 100))  # Random integer between 1 and 100

# Shuffle a list
my_list = [1, 2, 3, 4, 5]
cr.shuffle(my_list)
print(my_list)

# Sample from a population
print(cr.sample([1, 2, 3, 4, 5], 2))
```

---

## API Reference

### Initialization
```python
MZRandom(entropy_sources=None, prng_algorithm="xorshift1024")
```
- `entropy_sources`: Optional list of entropy-generating functions.
- `prng_algorithm`: Choose from `xorshift1024`, `pcg64`, or `chacha20`.

### Methods
- **Random Numbers**:
  - `random()`: Returns a random float in [0.0, 1.0).
  - `randint(a, b)`: Returns a random integer between `a` and `b` (inclusive).
  - `randrange(start, stop, step)`: Random value in a range.
- **Sequences**:
  - `choice(seq)`: Random element from a sequence.
  - `choices(population, k)`: `k` random choices (with replacement).
  - `shuffle(x)`: Shuffles a list in place.
  - `sample(population, k)`: `k` unique elements.
- **Distributions**:
  - `normalvariate(mu, sigma)`: Normal distribution.
  - `gammavariate(alpha, beta)`: Gamma distribution.
  - `triangular(low, high, mode)`: Triangular distribution.

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.

---

## License

MZRandom is licensed under the MIT License.

---

# MZRandom: کتابخانه‌ای جامع برای اعداد تصادفی

MZRandom یک کتابخانه قدرتمند و پرکاربرد برای تولید اعداد تصادفی در زبان پایتون است. این کتابخانه با استفاده از منابع متعدد انتروپی و الگوریتم‌های پیشرفته، قابلیت‌های گسترده‌ای ارائه می‌دهد.

---

## ویژگی‌ها

- **انتروپی بالا**: ترکیب منابع مختلف مانند زمان سیستم، وضعیت OS و اطلاعات حافظه.
- **الگوریتم‌های قابل تنظیم**: پشتیبانی از Xorshift1024، PCG64، و ChaCha20.
- **قابلیت‌های گسترده**:
  - تولید اعداد تصادفی اعشاری و صحیح
  - جابجایی و نمونه‌گیری از داده‌ها
  - توزیع‌های آماری (نرمال، گاما و غیره)
- **ایمن در برابر چند رشته‌ای (Thread-Safe)**: عملیات ایمن در محیط‌های چند رشته‌ای.

---

## نصب

```bash
pip install mzrandom
```

---

## استفاده

### مثال ساده

```python
from mzrandom import MZRandom

cr = MZRandom(prng_algorithm="pcg64")

# تولید اعداد تصادفی
print(cr.random())  # عدد اعشاری بین 0.0 و 1.0
print(cr.randint(1, 100))  # عدد صحیح بین 1 و 100

# جابجایی یک لیست
my_list = [1, 2, 3, 4, 5]
cr.shuffle(my_list)
print(my_list)

# نمونه‌گیری از یک مجموعه
print(cr.sample([1, 2, 3, 4, 5], 2))
```

---

## راهنمای API

### مقداردهی اولیه
```python
MZRandom(entropy_sources=None, prng_algorithm="xorshift1024")
```
- `entropy_sources`: لیستی از توابع تولید انتروپی (اختیاری).
- `prng_algorithm`: انتخاب بین `xorshift1024`، `pcg64`، یا `chacha20`.

### متدها
- **اعداد تصادفی**:
  - `random()`: عدد اعشاری تصادفی در بازه [0.0, 1.0).
  - `randint(a, b)`: عدد صحیح تصادفی بین `a` و `b` (شامل هر دو).
  - `randrange(start, stop, step)`: مقدار تصادفی از یک بازه.
- **دنباله‌ها**:
  - `choice(seq)`: یک عنصر تصادفی از دنباله.
  - `choices(population, k)`: `k` انتخاب تصادفی (با جایگزینی).
  - `shuffle(x)`: جابجایی لیست به صورت درجا.
  - `sample(population, k)`: `k` عنصر منحصر به فرد.
- **توزیع‌ها**:
  - `normalvariate(mu, sigma)`: توزیع نرمال.
  - `gammavariate(alpha, beta)`: توزیع گاما.
  - `triangular(low, high, mode)`: توزیع مثلثی.

---

## همکاری در توسعه

برای همکاری، لطفاً یک Issue باز کنید یا درخواست Pull Request ارسال کنید.

---

## مجوز

MZRandom تحت مجوز MIT ارائه شده است.

