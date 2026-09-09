# 📌 Шпаргалка по LaTeX (Математический синтаксис для Obsidian и отчётов)

> **Как использовать формулы в Obsidian / Markdown:**
> - **Внутри строки (inline):** `$ ... $` (например, `$x \in \mathbb{R}$` $\to$ $x \in \mathbb{R}$)
> - **Отдельной строкой по центру (block):** `$$ ... $$`
> - **Обычный текст внутри формулы:** `\text{ваш текст}` (например, `$\forall x \in \mathbb{R} \text{ верно, что } x^2 \ge 0$`)

---

## 1. 🔤 Логика, кванторы и связки

| Обозначение | LaTeX код | Как читать (RU) | How to read (EN) |
| :---: | :--- | :--- | :--- |
| $\forall$ | `\forall` | Для любого / для каждого | For all / For every |
| $\exists$ | `\exists` | Существует | There exists |
| $\exists!$ | `\exists!` | Существует и единственен | There exists a unique |
| $\nexists$ | `\nexists` | Не существует | There does not exist |
| $\neg$ | `\neg` | Отрицание (НЕ) | Not / Negation |
| $\implies$ | `\implies` или `\Rightarrow` | Следовательно / влечет | Implies / If... then... |
| $\iff$ | `\iff` или `\Leftrightarrow` | Тогда и только тогда | If and only if (iff) |
| $\land$ | `\land` | Логическое И (конъюнкция) | And |
| $\lor$ | `\lor` | Логическое ИЛИ (дизъюнкция) | Or |
| $\blacksquare$ | `\blacksquare` или `\square` | Конец доказательства (Q.E.D.) | End of proof |

---

## 2. 📦 Теория множеств

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
| $\{ \dots \}$ | `\{ \dots \}` | `\{1, 2, 3\}` | $\{1, 2, 3\}$ | **Важно:** фигурные скобки экранируются `\{` и `\}` |

### Числовые множества (`\mathbb{...}`)
* `\mathbb{N}` $\to \mathbb{N}$ — натуральные числа ($\{1, 2, 3, \dots\}$)
* `\mathbb{Z}` $\to \mathbb{Z}$ — целые числа ($\{\dots, -1, 0, 1, \dots\}$)
* `\mathbb{Q}` $\to \mathbb{Q}$ — рациональные числа (дроби)
* `\mathbb{R}` $\to \mathbb{R}$ — вещественные (действительные) числа
* `\mathbb{C}` $\to \mathbb{C}$ — комплексные числа

---

## 3. 🎯 Отображения и функции (Mappings & Functions)

| Обозначение | LaTeX код | Описание / Description |
| :---: | :--- | :--- |
| $f: X \to Y$ | `f: X \to Y` | Отображение из $X$ в $Y$ ($f$ from $X$ to $Y$) |
| $x \mapsto f(x)$ | `x \mapsto f(x)` | Элемент $x$ переходит в $f(x)$ ($x$ maps to $f(x)$) |
| $g \circ f$ | `g \circ f` | Композиция отображений (Composition) |
| $f^{-1}$ | `f^{-1}` | Обратное отображение (Inverse mapping) |
| $\text{id}_X$ | `\text{id}_X` | Тождественное отображение (Identity mapping) |
| $\operatorname{Im} f$ | `\operatorname{Im} f` | Образ отображения (Image of $f$) |

---

## 4. ⚖️ Отношения и сравнения

| Знак | LaTeX код | Значение |
| :---: | :--- | :--- |
| $\le$ | `\le` или `\leq` | Меньше либо равно (Less than or equal to) |
| $\ge$ | `\ge` или `\geq` | Больше либо равно (Greater than or equal to) |
| $\neq$ | `\neq` или `\ne` | Не равно (Not equal) |
| $\approx$ | `\approx` | Приблизительно равно |
| $\sim$ | `\sim` | Эквивалентно / отношение эквивалентности |
| $\equiv$ | `\equiv` | Тождественно равно / сравнимо по модулю |

---

## 5. 📐 Алгебраические конструкции

| Конструкция | LaTeX код | Пример | Результат |
| :--- | :--- | :--- | :---: |
| **Дроби** | `\frac{числитель}{знаменатель}` | `\frac{a + b}{c}` | $\frac{a + b}{c}$ |
| **Степени** | `x^{выражение}` | `x^{2}` или `x^{n+1}` | $x^2, x^{n+1}$ |
| **Индексы** | `x_{выражение}` | `x_1` или `a_{i, j}` | $x_1, a_{i, j}$ |
| **Модуль** | `\lvert x \rvert` или `\|x\|` | `\lvert x_1 - x_2 \rvert` | $\lvert x_1 - x_2 \rvert$ |
| **Корень** | `\sqrt{x}` или `\sqrt[n]{x}` | `\sqrt{x^2 + y^2}` | $\sqrt{x^2 + y^2}$ |
| **Бесконечность** | `\infty` | `[0, +\infty)` | $[0, +\infty)$ |
| **Сумма** | `\sum_{i=1}^n` | `\sum_{i=1}^n x_i` | $\sum_{i=1}^n x_i$ |
| **Предел** | `\lim_{x \to 0}` | `\lim_{n \to \infty} \frac{1}{n}` | $\lim_{n \to \infty} \frac{1}{n}$ |

---

## 6. 🇬🇷 Популярные греческие буквы

* $\alpha, \beta, \gamma$ $\to$ `\alpha, \beta, \gamma`
* $\delta, \varepsilon$ $\to$ `\delta, \varepsilon` *(эпсилон для пределов в матане!)*
* $\lambda, \mu$ $\to$ `\lambda, \mu` *(собственные значения в линале)*
* $\pi$ $\to$ `\pi`
* $\sigma$ $\to$ `\sigma`
* $\omega, \Omega$ $\to$ `\omega, \Omega`
