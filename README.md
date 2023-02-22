![Tec de Monterrey](images/logotecmty.png)
# Analysis and Design of Advanced Algorithms (TC2038)

```
<program> ::= <statement-sequence>

<statement-sequence> ::= <statement> <statement-sequence>
<statement-sequence> ::= ' '

<statement> ::=
  <simple-statement> |
  <structured-statement>

<simple-statement> ::=
  <declaration-statement> |
  <assignment-statement> |
  <movement-statement> |
  <drawing-statement> |
  <text-statement>
  
<declaration-statement> ::=
  VAR <identifier> <identifier-list>
  
<identifier-list> ::= ',' <identifier> <identifier-list>
<identifier-list> ::= ' '

<assigment-statement> ::= <identifier> ':''=' <expression>

<movement-statement> ::=
      <forward-statement> |
      <backward-statement> |
      <right-statement> |
      <left-statement> |
      <setx-statement> |
      <sety-statement> |
      <setxy-statement> |
      HOME
<forward-statement> ::=  (FORWARD | FD) <expression>
<backward-statement> ::= (BACKWARD | BK) <expression>
<right-statement> ::= (RIGHT | RT) <expression>
<left-statement> ::= (LEFT | LT) <expression>
<setx-statement> ::= SETX <expression>
<sety-statement> ::= SETY <expression>
<setxy-statement> ::= SETXY <expression> <expression>

<drawing-statement> :=
  <clear-statement> |
  <circle-statement> |
  <arc-statement> |
  <penup-staement> |
  <pendown-statement> |
  <color-statement> |
  <penwidth-statement>
<clear-statement> ::= (CLEAR | CLS)
<circle-statement> ::= CIRCLE <expression>
<arc-statement> ::= ARC <expression>
<penup-statement> ::= (PENUP | PU)
<pendown-statement> ::= (PENDOWN | PD)
<color-statement> ::= COLOR <expression> <expression> <expression>
<penwidth-statement> ::= PENWIDTH <expression>

<text-statement> ::= PRINT '[' <element> <element-list> ']'
element := <string> | <expression>
<element-list> := ',' <element> <element-list>
<element-list> := ' '

<structured-statement> ::=
  <repetitive-statement> |
  <conditional-statement>
<repetitive-statement> ::= 
  REPEAT <expression> '[' <statement-sequence> ']'
conditional-statement ::=
  <if-statement> |
  <if-else-statement>
<if-statement> ::= 
  IF <expression> '[' <if-true> ']'
<if-else-statement> ::= 
  IFELSE <expression> '[' <if-true> ']' '[' <if-false> ']'
<if-true> ::= <statement-sequence>
<if-false> ::= <statement-sequence>

<expression> ::= <conditional-expression>

<conditional-expression> ::= 
	<conditional-term> <extended-conditional-expression>
<extended-conditional-expression> ::=
	OR <conditional-term> <extended-conditional-expression>
<extended-conditional-expression> ::= ' '

<conditional-term> ::= 
	<equality-expression> <extended-conditional-term>
<extended-conditional-term> ::= 
	AND <equality-expression> <extended-conditional-term>
<extended-boolean-term> ::= ' '

<equality-expression> ::=
	<relational-expression> <extended-equality-expression>
<extended-equality-expression> := 
	'=' <relational-expression> <extended-equality-expression>
<extended-equality-expression> := 
	'<''>' <relational-expression> <extended-equality-expression>
<extended-equality-expression> ::= ' '

<relational-expression> ::= 
	<additive-expression> <extended-relational-expression>
<extended-relational-expression> :=
	'<' <additive-expression> <extended-relational-expression>
<extended-relational-expression> ::=
	'<''=' <additive-expression> <extended-relational-expression>
<extended-relational-expression> :=
	'>' <additive-expression> <extended-relational-expression>
<extended-relational-expression> ::=
	'>''=' <additive-expression> <extended-relational-expression>
<extended-relational-expression> ::= ' '
	
<additive-expression> ::= 
	<multiplicative-expression> <extended-additive-expression>
<extended-additive-expression> ::=
	'+'  <multiplicative-expression> <extended-additive-expression>
<extended-additive-expression> ::=
	'-'  <multiplicative-expression> <extended-additive-expression>
<extended-additive-expression> ::= ' '
	
<multiplicative-expression> ::=
	<unary-expression> <extended-multiplicative-expression>
<extended-multiplicative-expression> ::=
	'*' <unary-expression> <extended-multiplicative-expression>
<extended-multiplicative-expression> ::=
	'/' <unary-expression> <extended-multiplicative-expression>
<extended-multiplicative-expression> ::=
	MOD <unary-expression> <extended-multiplicative-expression>
<extended-multiplicative-expression> ::= ' '
	
<unary-expression> ::= 
	'-' <unary-expression> ||
	'!' <unary-expression> ||
	<primary-expression>

<primary-expression> ::= 
	<identifier> ||
	<number> ||
	<true>	||
	<false> || 
	'(' <expression> ')'
  
<identifier> ::= <letter> <characters>
<characters> ::= (<letter> | <digit>) <characters>
<characters> ::= ' '

<number> ::= <integer-number> | <real-number>
<integer-number> ::= <digit-sequence>
<digit-sequence> ::= <digit> <digits>
<digits> ::= <digit> <digits>
<digits> ::= ' '

<true> ::= '#''t'
<false> ::= '#''f'

<letter> ::= ['A'-'Z'] | ['a'-'z']
<digit> ::= ['0'-'9']
<string> ::= '"' <string-character> <more-string-chracters> '"'
<<more-string-chracters> ::= <string-character> <more-string-chracters>
<more-string-chracters> ::= ' '
<string-character> ::= <any-character-except-quote>
```
