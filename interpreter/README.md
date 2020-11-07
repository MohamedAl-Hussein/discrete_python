# **Description**
A simple math interpreter for propositional logic.

## **Tokens**

* `[a-zA-Z]` propositional variable
* `&&` logical and
* `||` logical or
* `~` negation
* `^` exclusive or
* `-->` implication
* `<-->` bi-conditional
* `==` logical equivalence
* `(` left parentheses
* `)` right parentheses
* `forall` universal quantifier
* `exists` existential quantifier

## **Operator Precedence**

1. `forall`, `exists`
2. `~`
3. `&&`
4. `||`
5. `-->`
6. `<-->`

***Note:** Anything enclosed in parentheses takes highest precedence.*

## **Grammar Rules**

* **Variable**: A character or sequence of characters
* **Binary Expression**: Two **Variable** or **Compound Expression** types separated by `&&`, `||`, `^`, `-->`, or `<-->`
* **Unary Expression**: `~` followed by a **Variable**, `(`, or `~`
* **Quantification**: `forall` or `exists` followed by a **Variable** or `(`
* **Compound Expression**: A combination of two or more **Binary Expression** or **Unary Expression** types
* **Comparison**: Two **Variable**, **Unary**, **Binary**, **Quantification**, or **Compound Expression** types separated by `==`