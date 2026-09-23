---
title: "Полная шпаргалка по LaTeX (KaTeX) для ITMO Software Engineering"
tags:
  - latex
  - katex
  - формулы
  - шпаргалка
  - математика
  - аисд
  - линал
  - матан
  - дискретка
---

# 📌 Полная шпаргалка по LaTeX / KaTeX (ИТМО • 1 семестр)

> **Как использовать формулы в Obsidian / Markdown:**
> - **Внутри строки (inline):** `$ ... $` (например, `$x \in \mathbb{R}$` $\to$ $x \in \mathbb{R}$)
> - **Отдельной строкой по центру (display/block):** `$$ ... $$`
> - **Обычный текст внутри формулы:** `\text{ваш текст}` (например, `$\forall x \in \mathbb{R} \text{ верно, что } x^2 \ge 0$`)
> - **Пробелы внутри формул:** `\,` (тонкий), `\:` (средний), `\;` (толстый), `\quad` (пробел шириной M), `\qquad` (двойной широкий пробел), `\!` (отрицательный пробел/стяжка)
> - **Авторазмер скобок:** `\left( \frac{a}{b} \right)` автоматически подгоняет высоту скобок под содержимое!

---

## 1. ⚙️ Шрифты, акценты и оформление

| LaTeX код | Результат | Назначение / Смысл |
| :--- | :---: | :--- |
| `\mathbb{R}, \mathbb{N}, \mathbb{Z}, \mathbb{C}` | $\mathbb{R}, \mathbb{N}, \mathbb{Z}, \mathbb{C}$ | Числовые множества (Blackboard bold) |
| `\mathcal{O}, \mathcal{P}, \mathcal{F}` | $\mathcal{O}, \mathcal{P}, \mathcal{F}$ | Каллиграфический шрифт (булеан, классы) |
| `\mathbf{v}, \mathbf{0}, \mathbf{A}` | $\mathbf{v}, \mathbf{0}, \mathbf{A}$ | Полужирный шрифт (векторы, матрицы) |
| `\mathfrak{g}, \mathfrak{S}` | $\mathfrak{g}, \mathfrak{S}$ | Готический шрифт (алгебры, группы перестановок) |
| `\operatorname{rank}(A), \operatorname{lcm}(a, b)` | $\operatorname{rank}(A), \operatorname{lcm}(a, b)$ | Пользовательские операторы прямым шрифтом |
| `\bar{x}, \overline{AB}` | $\bar{x}, \overline{AB}$ | Черта сверху (комплексное сопряжение, отрезок) |
| `\hat{x}, \tilde{x}, \vec{v}` | $\hat{x}, \tilde{x}, \vec{v}$ | Шляпка, тильда, вектор |
| `\dot{x}, \ddot{x}` | $\dot{x}, \ddot{x}$ | Первая и вторая производная по времени |

---

## 2. ⚡ Алгоритмы и структуры данных (АиСД • Асимптотики)

| Обозначение | LaTeX код | Пример кода | Результат | Смысл / Назначение |
| :---: | :--- | :--- | :---: | :--- |
| $O(g(n))$ | `O(g(n))` | `O(n \log n)` | $O(n \log n)$ | Верхняя асимптотическая оценка |
| $\Omega(g(n))$ | `\Omega(g(n))` | `\Omega(n \log n)` | $\Omega(n \log n)$ | Нижняя асимптотическая оценка |
| $\Theta(g(n))$ | `\Theta(g(n))` | `\Theta(n^2)` | $\Theta(n^2)$ | Точная двусторонняя оценка |
| $o(g(n))$ | `o(g(n))` | `f(n) = o(n^2)` | $f(n) = o(n^2)$ | Строго медленнее (малое «о») |
| $\omega(g(n))$ | `\omega(g(n))` | `f(n) = \omega(n)` | $f(n) = \omega(n)$ | Строго быстрее (малая омега) |
| $\log_b a$ | `\log_b a` | `\log_2 7 \approx 2{,}81` | $\log_2 7 \approx 2{,}81$ | Логарифм по основанию $b$ |
| $\ln n, \lg n$ | `\ln n, \lg n` | `\ln n, \lg n` | $\ln n, \lg n$ | Натуральный и двоичный/десятичный логарифм |
| $\lfloor x \rfloor$ | `\lfloor x \rfloor` | `\lfloor n / 2 \rfloor` | $\lfloor n / 2 \rfloor$ | Округление вниз («пол», floor) |
| $\lceil x \rceil$ | `\lceil x \rceil` | `\lceil n / 2 \rceil` | $\lceil n / 2 \rceil$ | Округление вверх («потолок», ceil) |
| $\leftarrow$ | `\leftarrow` | `x \leftarrow A[0]` | $x \leftarrow A[0]$ | Присваивание в псевдокоде |
| $T(n)$ | `T(n) = a T(n/b) + \Theta(n^c)` | *формула* | $T(n) = a T(n/b) + \Theta(n^c)$ | Рекуррента Мастер-теоремы |

---

## 3. 🔢 Дискретная математика (Логика, Множества, Отношения)

### Логика высказываний и предикаты

| Обозначение | LaTeX код | Как читать (RU) | How to read (EN) |
| :---: | :--- | :--- | :--- |
| $\forall$ | `\forall` | Для любого / для каждого | For all / For every |
| $\exists$ | `\exists` | Существует | There exists |
| $\exists!$ | `\exists!` | Существует и единственен | There exists a unique |
| $\nexists$ | `\nexists` | Не существует | There does not exist |
| $\neg$ | `\neg` | Отрицание (НЕ) | Negation / Not |
| $\implies$ | `\implies` или `\Rightarrow` | Следовательно / влечет | Implies / If... then... |
| $\iff$ | `\iff` или `\Leftrightarrow` | Тогда и только тогда (ТТТ) | If and only if (iff) |
| $\land$ | `\land` | Конъюнкция (И) | Conjunction (And) |
| $\lor$ | `\lor` | Дизъюнкция (ИЛИ) | Disjunction (Or) |
| $\oplus$ | `\oplus` | Исключающее ИЛИ (XOR) | Exclusive Or |
| $\top, \bot$ | `\top, \bot` | Истина (True), Ложь (False) | Tautology, Contradiction |
| $\vdash, \vDash$ | `\vdash, \vDash` | Выводимо, Общезначимо | Provable, Semantic entailment |
| $\blacksquare$ | `\blacksquare` или `\square` | Конец доказательства (ч.т.д.) | Q.E.D. |

### Множества и операции над ними

| Обозначение | LaTeX код | Пример кода | Результат | Смысл / Meaning |
| :---: | :--- | :--- | :---: | :--- |
| $\in, \notin$ | `\in, \notin` | `x \in A, y \notin B` | $x \in A, y \notin B$ | Принадлежит / не принадлежит |
| $\subseteq, \subsetneq$ | `\subseteq, \subsetneq` | `A \subseteq B, A \subsetneq B` | $A \subseteq B, A \subsetneq B$ | Подмножество / строгое подмножество |
| $\varnothing$ | `\varnothing` или `\emptyset` | `A \cap B = \varnothing` | $A \cap B = \varnothing$ | Пустое множество |
| $\cup, \cap$ | `\cup, \cap` | `A \cup B, A \cap B` | $A \cup B, A \cap B$ | Объединение, пересечение |
| $\setminus, \triangle$ | `\setminus, \triangle` | `A \setminus B, A \triangle B` | $A \setminus B, A \triangle B$ | Разность, симметрическая разность |
| $\times$ | `\times` | `A \times B` | $A \times B$ | Декартово произведение |
| $\mathcal{P}(A), 2^A$ | `\mathcal{P}(A), 2^A` | `\mathcal{P}(X)` | $\mathcal{P}(X)$ | Булеан (множество всех подмножеств) |
| $\mid$ | `\mid` | `\{x \in X \mid P(x)\}` | $\{x \in X \mid P(x)\}$ | Вертикальная черта условия (с пробелами!) |
| $\{ \dots \}$ | `\{ \dots \}` | `\{1, 2, 3\}` | $\{1, 2, 3\}$ | Фигурные скобки экранируются `\{` `\}` |

### Отношения, порядки и отображения

| Обозначение | LaTeX код | Значение / Смысл |
| :---: | :--- | :--- |
| $a \sim b$ | `a \sim b` | Отношение эквивалентности |
| $[a]_\sim, X/\sim$ | `[a]_\sim, X/\sim` | Класс эквивалентности, фактор-множество |
| $\preceq, \succeq$ | `\preceq, \succeq` | Отношение частичного порядка |
| $\prec, \succ$ | `\prec, \succ` | Строгий порядок |
| $\sqsubseteq, \sqsupseteq$ | `\sqsubseteq, \sqsupseteq` | Информационный порядок / решетка |
| $\inf, \sup$ | `\inf A, \sup A` | Точная нижняя / верхняя грань (инфимум, супремум) |
| $f: X \to Y$ | `f: X \to Y` | Отображение из $X$ в $Y$ |
| $x \mapsto f(x)$ | `x \mapsto f(x)` | Элемент переходит в образ |
| $g \circ f$ | `g \circ f` | Композиция отображений |
| $f^{-1}$ | `f^{-1}` | Обратное отображение / прообраз |

---

## 4. 📐 Линейная алгебра и аналитическая геометрия

### Векторы и скалярные произведения

| Конструкция | LaTeX код | Пример | Результат |
| :--- | :--- | :--- | :---: |
| **Вектор со стрелкой** | `\vec{v}, \vec{AB}` | `\vec{v} = (x, y, z)` | $\vec{v} = (x, y, z)$ |
| **Жирный вектор** | `\mathbf{v}, \mathbf{x}` | `\mathbf{v} \in \mathbb{R}^n` | $\mathbf{v} \in \mathbb{R}^n$ |
| **Скалярное произведение** | `\langle u, v \rangle` или `u \cdot v` | `\langle \mathbf{u}, \mathbf{v} \rangle = 0` | $\langle \mathbf{u}, \mathbf{v} \rangle = 0$ |
| **Векторное произведение** | `u \times v` или `[u, v]` | `\vec{a} \times \vec{b}` | $\vec{a} \times \vec{b}$ |
| **Норма / длина вектора** | `\| \mathbf{v} \|` | `\|\mathbf{v}\| = \sqrt{\langle \mathbf{v}, \mathbf{v} \rangle}` | $\|\mathbf{v}\| = \sqrt{\langle \mathbf{v}, \mathbf{v} \rangle}$ |
| **Линейная оболочка** | `\operatorname{span}(v_1, \dots, v_k)` | `\operatorname{span}(\mathbf{e}_1, \mathbf{e}_2)` | $\operatorname{span}(\mathbf{e}_1, \mathbf{e}_2)$ |
| **Размерность и ранг** | `\dim V, \operatorname{rank} A` | `\dim \operatorname{Ker} A + \operatorname{rank} A = n` | $\dim \operatorname{Ker} A + \operatorname{rank} A = n$ |

### Матрицы и определители

#### Матрица в круглых скобках (`pmatrix`):
```latex
A = \begin{pmatrix}
a_{11} & a_{12} & \dots & a_{1n} \\
a_{21} & a_{22} & \dots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \dots & a_{mn}
\end{pmatrix}
```
$$A = \begin{pmatrix} a_{11} & a_{12} & \dots & a_{1n} \\ a_{21} & a_{22} & \dots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \dots & a_{mn} \end{pmatrix}$$

#### Определитель матрицы (`vmatrix`):
```latex
\det A = \begin{vmatrix}
a & b \\
c & d
\end{vmatrix} = ad - bc
```
$$\det A = \begin{vmatrix} a & b \\ c & d \end{vmatrix} = ad - bc$$

#### Системы линейных уравнений (`cases`):
```latex
\begin{cases}
a_{11} x_1 + a_{12} x_2 + \dots + a_{1n} x_n = b_1 \\
a_{21} x_1 + a_{22} x_2 + \dots + a_{2n} x_n = b_2 \\
\dots \\
a_{m1} x_1 + a_{m2} x_2 + \dots + a_{mn} x_n = b_m
\end{cases}
```
$$\begin{cases} a_{11} x_1 + a_{12} x_2 + \dots + a_{1n} x_n = b_1 \\ a_{21} x_1 + a_{22} x_2 + \dots + a_{2n} x_n = b_2 \\ \dots \\ a_{m1} x_1 + a_{m2} x_2 + \dots + a_{mn} x_n = b_m \end{cases}$$

---

## 5. 📈 Математический анализ (Пределы, Производные, Интегралы)

| Конструкция | LaTeX код | Пример кода | Результат |
| :--- | :--- | :--- | :---: |
| **Дроби** | `\frac{a}{b}` или `\dfrac{a}{b}` | `\frac{x^2 - 1}{x - 1} = x + 1` | $\frac{x^2 - 1}{x - 1} = x + 1$ |
| **Корни** | `\sqrt{x}`, `\sqrt[n]{x}` | `\sqrt{x^2 + y^2}, \sqrt[3]{n}` | $\sqrt{x^2 + y^2}, \sqrt[3]{n}$ |
| **Сумма и произведение** | `\sum_{i=1}^n`, `\prod_{i=1}^n` | `\sum_{k=1}^n k = \frac{n(n+1)}{2}` | $\sum_{k=1}^n k = \frac{n(n+1)}{2}$ |
| **Предел последовательности** | `\lim_{n \to \infty}` | `\lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n = e` | $\lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n = e$ |
| **Односторонние пределы** | `\lim_{x \to x_0^+}, \lim_{x \to x_0^-}` | `\lim_{x \to 0^+} \frac{1}{x} = +\infty` | $\lim_{x \to 0^+} \frac{1}{x} = +\infty$ |
| **Критерий Коши / $\varepsilon-\delta$** | `\forall \varepsilon > 0\ \exists N \dots` | `\forall \varepsilon > 0\ \exists \delta > 0 \dots` | $\forall \varepsilon > 0\ \exists \delta > 0$ |
| **Производная** | `f'(x), \frac{df}{dx}, \frac{d^2 f}{dx^2}` | `\frac{d}{dx}(e^x) = e^x` | $\frac{d}{dx}(e^x) = e^x$ |
| **Частная производная** | `\frac{\partial f}{\partial x}` | `\frac{\partial f}{\partial x} + \frac{\partial f}{\partial y}` | $\frac{\partial f}{\partial x} + \frac{\partial f}{\partial y}$ |
| **Неопределенный интеграл** | `\int f(x)\,dx` | `\int \frac{1}{x}\,dx = \ln|x| + C` | $\int \frac{1}{x}\,dx = \ln|x| + C$ |
| **Определенный интеграл** | `\int_a^b f(x)\,dx` | `\int_0^1 x^2\,dx = \left. \frac{x^3}{3} \right|_0^1 = \frac{1}{3}` | $\int_0^1 x^2\,dx = \left. \frac{x^3}{3} \right|_0^1 = \frac{1}{3}` |
| **Подстановка пределов** | `\left. F(x) \right|_a^b` | `\left. \sin x \right|_0^\pi` | $\left. \sin x \right|_0^\pi$ |

---

## 6. 🏛️ Теория чисел, делимость и кольца вычетов

| Обозначение | LaTeX код | Пример кода | Результат | Смысл / Описание |
| :---: | :--- | :--- | :---: | :--- |
| $\mid$ | `\mid` | `a \mid b` | $a \mid b$ | $a$ делит $b$ (вертикальная черта оператора с пробелами) |
| $\nmid$ | `\nmid` | `a \nmid b` | $a \nmid b$ | $a$ не делит $b$ |
| $\equiv$ | `\equiv` | `a \equiv b \pmod n` | $a \equiv b \pmod n$ | Сравнимо по модулю $n$ |
| $\bmod$ | `\bmod` | `r = a \bmod b` | $r = a \bmod b$ | Остаток от деления (бинарная операция) |
| $\gcd$ | `\gcd(a, b)` | `\gcd(a, b) = 1` | $\gcd(a, b) = 1$ | Наибольший общий делитель (НОД, взаимно просты) |
| $\operatorname{lcm}$ | `\operatorname{lcm}(a, b)` | `\operatorname{lcm}(a, b) = \frac{ab}{\gcd(a, b)}` | $\operatorname{lcm}(a, b) = \frac{ab}{\gcd(a, b)}$ | Наименьшее общее кратное (НОК) |
| $\mathbb{Z}_n, \mathbb{Z}/n\mathbb{Z}$ | `\mathbb{Z}_n, \mathbb{Z}/n\mathbb{Z}` | `\mathbb{Z}_n` | $\mathbb{Z}_n$ | Кольцо / фактор-кольцо вычетов по модулю $n$ |
| $\mathbb{Z}_n^\times$ | `\mathbb{Z}_n^\times` | `\mathbb{Z}_p^\times \cong \mathbb{Z}_{p-1}` | $\mathbb{Z}_p^\times \cong \mathbb{Z}_{p-1}$ | Мультипликативная группа обратимых элементов |
| $[a]^{-1}$ | `[a]^{-1}` | `[3]^{-1} \equiv [5] \pmod 7` | $[3]^{-1} \equiv [5] \pmod 7$ | Обратный элемент по модулю |
| $\varphi(n)$ | `\varphi(n)` | `\varphi(p) = p - 1` | $\varphi(p) = p - 1$ | Функция Эйлера |

---

## 7. 🇬🇷 Греческий алфавит

| Строчная | Код | Прописная | Код | Название (RU) |
| :---: | :--- | :---: | :--- | :--- |
| $\alpha$ | `\alpha` | $A$ | `A` | Альфа |
| $\beta$ | `\beta` | $B$ | `B` | Бета |
| $\gamma$ | `\gamma` | $\Gamma$ | `\Gamma` | Гамма |
| $\delta$ | `\delta` | $\Delta$ | `\Delta` | Дельта |
| $\varepsilon, \epsilon$ | `\varepsilon, \epsilon` | $E$ | `E` | Эпсилон |
| $\zeta$ | `\zeta` | $Z$ | `Z` | Дзета |
| $\eta$ | `\eta` | $H$ | `H` | Эта |
| $\theta, \vartheta$ | `\theta, \vartheta` | $\Theta$ | `\Theta` | Тета |
| $\iota$ | `\iota` | $I$ | `I` | Йота |
| $\kappa$ | `\kappa` | $K$ | `K` | Каппа |
| $\lambda$ | `\lambda` | $\Lambda$ | `\Lambda` | Лямбда |
| $\mu$ | `\mu` | $M$ | `M` | Мю |
| $\nu$ | `\nu` | $N$ | `N` | Ню |
| $\xi$ | `\xi` | $\Xi$ | `\Xi` | Кси |
| $\pi, \varpi$ | `\pi, \varpi` | $\Pi$ | `\Pi` | Пи |
| $\rho, \varrho$ | `\rho, \varrho` | $P$ | `P` | Ро |
| $\sigma, \varsigma$ | `\sigma, \varsigma` | $\Sigma$ | `\Sigma` | Сигма |
| $\tau$ | `\tau` | $T$ | `T` | Тау |
| $\upsilon$ | `\upsilon` | $\Upsilon$ | `\Upsilon` | Ипсилон |
| $\varphi, \phi$ | `\varphi, \phi` | $\Phi$ | `\Phi` | Фи |
| $\chi$ | `\chi` | $X$ | `X` | Хи |
| $\psi$ | `\psi` | $\Psi$ | `\Psi` | Пси |
| $\omega$ | `\omega` | $\Omega$ | `\Omega` | Омега |

---

## 8. 🛡️ Частые ошибки и правила KaTeX в Obsidian

1. **Никогда не разрывайте inline-формулу переносом строки:**
   - ❌ Ошибка: `$x \in\n\mathbb{R}$` (Obsidian перестает воспринимать это как формулу).
   - ✅ Правильно: `$x \in \mathbb{R}$`.
2. **Никаких пустых строк внутри `$$ ... $$`:**
   - KaTeX ломается, если внутри блока формулы вставить пустую строку.
3. **Экранирование фигурных скобок:**
   - В LaTeX фигурные скобки `{}` служат для группировки аргументов. Чтобы отобразить саму скобку множества, пишите `\{` и `\}`:
   - `\{ 1, 2, 3 \}` $\implies \{ 1, 2, 3 \}$.
4. **Текст внутри формул:**
   - Всегда оборачивайте русские и английские слова в `\text{...}`:
   - `T(n) = \Theta(n^2) \quad \text{в худшем случае}` $\implies T(n) = \Theta(n^2) \quad \text{в худшем случае}$.
5. **Делимость и отношение:**
   - Пишите `a \mid b` вместо `a | b`, чтобы вокруг палочки делимости появились правильные математические отступы.
6. **Многоуровневые дроби:**
   - Для больших читаемых формул в блоках `$$ ... $$` используйте `\dfrac{a}{b}` вместо `\frac{a}{b}` — числитель и знаменатель не будут уменьшаться в размере.
