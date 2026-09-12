# 📌 Полная шпаргалка по LaTeX (Математический синтаксис для Obsidian, конспектов и отчётов)

> **Как использовать формулы в Obsidian / Markdown:**
> - **Внутри строки (inline):** `$ ... $` (например, `$x \in \mathbb{R}$` $\to$ $x \in \mathbb{R}$)
> - **Отдельной строкой по центру (display/block):** `$$ ... $$`
> - **Обычный текст внутри формулы:** `\text{ваш текст}` (например, `$\forall x \in \mathbb{R} \text{ верно, что } x^2 \ge 0$`)
> - **Пробелы внутри формул:** `\,` (тонкий), `\quad` (средний пробел), `\qquad` (двойной широкий пробел)

---

## 1. 🔤 Логика, кванторы и связки

| Обозначение | LaTeX код | Как читать (RU) | How to read (EN) |
| :---: | :--- | :--- | :--- |
| $\forall$ | `\forall` | Для любого / для каждого | For all / For every |
| $\exists$ | `\exists` | Существует | There exists |
| $\exists!$ | `\exists!` | Существует и единственен | There exists a unique |
| $\nexists$ | `\nexists` | Не существует | There does not exist |
| $]$ | `]` или `\text{Пусть }` | Пусть (допущение лектора) | Let / Suppose |
| $\neg$ | `\neg` | Отрицание (НЕ) | Not / Negation |
| $\implies$ | `\implies` или `\Rightarrow` | Следовательно / влечет | Implies / If... then... |
| $\iff$ | `\iff` или `\Leftrightarrow` | Тогда и только тогда | If and only if (iff) |
| $\land$ | `\land` | Логическое И (конъюнкция) | And |
| $\lor$ | `\lor` | Логическое ИЛИ (дизъюнкция) | Or |
| $\blacksquare$ | `\blacksquare` или `\square` | Конец доказательства (ч.т.д. / Q.E.D.) | End of proof |

---

## 2. 🔢 Теория чисел, делимость и кольца вычетов (Новое!)

| Обозначение | LaTeX код | Пример кода | Результат | Смысл / Описание |
| :---: | :--- | :--- | :---: | :--- |
| $\mid$ | `\mid` | `a \mid b` | $a \mid b$ | $a$ делит $b$ ($a$ divides $b$) *(именно `\mid`, а не обычный `|`, для правильных отступов!)* |
| $\nmid$ | `\nmid` | `a \nmid b` | $a \nmid b$ | $a$ не делит $b$ ($a$ does not divide $b$) |
| $\equiv$ | `\equiv` | `a \equiv b` | $a \equiv b$ | Сравнимо / тождественно равно |
| $\pmod n$ | `\pmod n` | `a \equiv b \pmod n` | $a \equiv b \pmod n$ | Сравнение по модулю $n$ (с круглыми скобками) |
| $\bmod$ | `\bmod` | `r = a \bmod b` | $r = a \bmod b$ | Остаток от деления (бинарная операция) |
| $\gcd$ | `\gcd(a, b)` | `\gcd(a, b) = 1` | $\gcd(a, b) = 1$ | Наибольший общий делитель (НОД) |
| $\operatorname{lcm}$ | `\operatorname{lcm}(a, b)` | `\operatorname{lcm}(a, b)` | $\operatorname{lcm}(a, b)$ | Наименьшее общее кратное (НОК) |
| $[a]$ | `[a]` или `\bar{a}` | `[a]_n` или `\overline{a}` | $[a]_n$ или $\overline{a}$ | Класс вычетов / класс эквивалентности |
| $[a]^{-1}$ | `[a]^{-1}` | `[3]^{-1} = [5]` | $[3]^{-1} = [5]$ | Обратный элемент в кольце вычетов |
| $\mathbb{Z}_n$ | `\mathbb{Z}_n` | `\mathbb{Z}_n` | $\mathbb{Z}_n$ | Кольцо вычетов по модулю $n$ |
| $\mathbb{Z}/n\mathbb{Z}$ | `\mathbb{Z}/n\mathbb{Z}` | `\mathbb{Z} / n\mathbb{Z}` | $\mathbb{Z} / n\mathbb{Z}$ | Фактор-кольцо вычетов |
| $\mathbb{Z}_n^\times$ | `\mathbb{Z}_n^\times` | `\mathbb{Z}_n^\times` | $\mathbb{Z}_n^\times$ | Мультипликативная группа обратимых элементов |

---

## 3. 📦 Теория множеств и фактор-множества

| Обозначение | LaTeX код | Пример кода | Результат | Смысл / Meaning |
| :---: | :--- | :--- | :---: | :--- |
| $\in$ | `\in` | `x \in A` | $x \in A$ | $x$ принадлежит $A$ ($x$ belongs to $A$) |
| $\notin$ | `\notin` | `x \notin A` | $x \notin A$ | $x$ не принадлежит $A$ |
| $\subseteq$ | `\subseteq` | `A \subseteq B` | $A \subseteq B$ | $A$ — подмножество $B$ ($A$ is a subset of $B$) |
| $\subsetneq$ | `\subsetneq` или `\subset` | `A \subsetneq B` | $A \subsetneq B$ | Строгое подмножество (Proper subset) |
| $\not\subseteq$ | `\not\subseteq` | `A \not\subseteq B` | $A \not\subseteq B$ | Не является подмножеством |
| $\varnothing$ | `\varnothing` или `\emptyset` | `A = \varnothing` | $A = \varnothing$ | Пустое множество (Empty set) |
| $\cup$ | `\cup` | `A \cup B` | $A \cup B$ | Объединение (Union) |
| $\cap$ | `\cap` | `A \cap B` | $A \cap B$ | Пересечение (Intersection) |
| $\setminus$ | `\setminus` | `A \setminus B` | $A \setminus B$ | Разность множеств (Set difference) |
| $\triangle$ | `\triangle` | `A \triangle B` | $A \triangle B$ | Симметрическая разность |
| $\times$ | `\times` | `A \times B` | $A \times B$ | Декартово произведение (Cartesian product) |
| $X / \sim$ | `X / \sim` | `X / \sim` | $X / \sim$ | Фактор-множество по отношению эквивалентности |
| $\{ \dots \}$ | `\{ \dots \}` | `\{x \in X \mid P(x)\}` | $\{x \in X \mid P(x)\}$ | **Важно:** фигурные скобки экранируются `\{` и `\}` |

### Числовые множества (`\mathbb{...}`)
* `\mathbb{N}` $\to \mathbb{N}$ — натуральные числа ($\{1, 2, 3, \dots\}$)
* `\mathbb{Z}` $\to \mathbb{Z}$ — целые числа ($\{\dots, -1, 0, 1, \dots\}$)
* `\mathbb{Q}` $\to \mathbb{Q}$ — рациональные числа (дроби)
* `\mathbb{R}` $\to \mathbb{R}$ — вещественные (действительные) числа
* `\mathbb{C}` $\to \mathbb{C}$ — комплексные числа

---

## 4. 🎯 Отображения и функции (Mappings & Functions)

| Обозначение | LaTeX код | Описание / Description |
| :---: | :--- | :--- |
| $f: X \to Y$ | `f: X \to Y` | Отображение из $X$ в $Y$ ($f$ from $X$ to $Y$) |
| $x \mapsto f(x)$ | `x \mapsto f(x)` | Элемент $x$ переходит в $f(x)$ ($x$ maps to $f(x)$) |
| $g \circ f$ | `g \circ f` | Композиция отображений (Composition) |
| $f^{-1}$ | `f^{-1}` | Обратное отображение / прообраз (Inverse mapping / Preimage) |
| $\text{id}_X$ | `\text{id}_X` | Тождественное отображение (Identity mapping) |
| $\operatorname{Im} f$ | `\operatorname{Im} f` | Образ отображения (Image of $f$) |
| $\operatorname{Ker} f$ | `\operatorname{Ker} f` | Ядро отображения (Kernel of $f$) |

---

## 5. ⚖️ Отношения, порядки и экстремумы

| Знак | LaTeX код | Значение |
| :---: | :--- | :--- |
| $\le, \ge$ | `\le`, `\ge` | Меньше/больше либо равно |
| $\neq$ | `\neq` или `\ne` | Не равно (Not equal) |
| $\approx$ | `\approx` | Приблизительно равно |
| $\sim$ | `\sim` | Отношение эквивалентности (Equivalent) |
| $\preceq, \succeq$ | `\preceq`, `\succeq` | Отношение частичного порядка (Partial order) |
| $\inf, \sup$ | `\inf A`, `\sup A` | Точная нижняя / верхняя грань (Infimum, Supremum) |
| $\min, \max$ | `\min A`, `\max A` | Минимум / максимум множества |

---

## 6. 📐 Алгебраические конструкции и математический анализ

| Конструкция | LaTeX код | Пример | Результат |
| :--- | :--- | :--- | :---: |
| **Дроби** | `\frac{числ}{знам}` | `\frac{a + b}{c}` | $\frac{a + b}{c}$ |
| **Степени и индексы** | `x^{n+1}_{i, j}` | `x^{2}_{0}` | $x^2_0$ |
| **Модуль / норма** | `\lvert x \rvert` или `\|x\|` | `\lvert a - b \rvert` | $\lvert a - b \rvert$ |
| **Корень** | `\sqrt{x}` или `\sqrt[n]{x}` | `\sqrt[3]{x + 1}` | $\sqrt[3]{x + 1}$ |
| **Бесконечность** | `\infty` | `(-\infty, +\infty)` | $(-\infty, +\infty)$ |
| **Сумма и произведение** | `\sum`, `\prod` | `\sum_{k=1}^n k^2` | $\sum_{k=1}^n k^2$ |
| **Предел** | `\lim_{n \to \infty}` | `\lim_{n \to \infty} \frac{1}{n} = 0` | $\lim_{n \to \infty} \frac{1}{n} = 0$ |
| **Биномиальный коэф.** | `\binom{n}{k}` | `\binom{n}{k}` | $\binom{n}{k}$ |
| **Многоточие в суммах** | `\dots` или `\cdots` | `a_1 + a_2 + \dots + a_n` | $a_1 + a_2 + \dots + a_n$ |
| **Многоточие в списках** | `\ldots` | `1, 2, \ldots, n` | $1, 2, \ldots, n$ |

---

## 7. 🔲 Системы уравнений и матрицы (Для Линейной Алгебры)

### Системы уравнений / условия по случаям (`cases`):
```latex
\begin{cases}
a_1 x + b_1 y = c_1 \\
a_2 x + b_2 y = c_2
\end{cases}
```
$$\begin{cases} a_1 x + b_1 y = c_1 \\ a_2 x + b_2 y = c_2 \end{cases}$$

### Матрицы в круглых скобках (`pmatrix`):
```latex
A = \begin{pmatrix}
1 & 2 & 3 \\
0 & 4 & 5 \\
0 & 0 & 6
\end{pmatrix}
```
$$A = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 4 & 5 \\ 0 & 0 & 6 \end{pmatrix}$$

### Определитель матрицы (`vmatrix`):
```latex
\det A = \begin{vmatrix}
a & b \\
c & d
\end{vmatrix} = ad - bc
```
$$\det A = \begin{vmatrix} a & b \\ c & d \end{vmatrix} = ad - bc$$

---

## 8. 🇬🇷 Греческие буквы

| Буква | LaTeX | Буква | LaTeX | Буква | LaTeX |
| :---: | :--- | :---: | :--- | :---: | :--- |
| $\alpha$ | `\alpha` | $\beta$ | `\beta` | $\gamma, \Gamma$ | `\gamma, \Gamma` |
| $\delta, \Delta$ | `\delta, \Delta` | $\varepsilon, \epsilon$ | `\varepsilon, \epsilon` | $\zeta$ | `\zeta` |
| $\eta$ | `\eta` | $\theta, \Theta$ | `\theta, \Theta` | $\lambda, \Lambda$ | `\lambda, \Lambda` |
| $\mu$ | `\mu` | $\pi, \Pi$ | `\pi, \Pi` | $\rho$ | `\rho` |
| $\sigma, \Sigma$ | `\sigma, \Sigma` | $\tau$ | `\tau` | $\varphi, \phi, \Phi$ | `\varphi, \phi, \Phi` |
| $\psi, \Psi$ | `\psi, \Psi` | $\omega, \Omega$ | `\omega, \Omega` | $\xi, \Xi$ | `\xi, \Xi` |
