
# ΙΧΘΥΣ / ἰχθῦς / ixqus

* νεκροΐχθυς (deadfish)
* ἀρχαῖος ἰχθῦς (ancient fish)
* παλαιός ἰχθῦς (old fish)
* γάρος (aged, fermented fish)
* ἰχθῦς σηπτός (rotten fish)

ΙΧΘΥΣ means 'fish' in Classical Greek. It is a derivative of firefly431's [Deadfish x](https://esolangs.org/wiki/Deadfish_x), and therefore a superset of Jonathan Todd Skinner's original [Deadfish](https://esolangs.org/wiki/Deadfish).

### Motivation
I wanted to experiment with creating a reduced instruction set esoteric (+joke) programming language that made use of archaic languages and alphabets (yay Unicode!). Deadfish seemed an appealing base, and Deadfish x seemed like a powerful extension by adding 'functions', even though I don't believe they are functions in a strict sense.

### ΙΧΘΥΣ Commands

| letter | term | action | CAPITAL | CAPITAL action |
| --     | --   | --     | --      | --             |
| ι | ἵστημι (raise / set up) | x+1 | Ι | Begin statement def |
| χ | χάζω (draw back)        | x-1 | Χ | Set x to 0 |
| θ | Θʹ (9) a square number   | x*x | Θ | End statement def (Θέτε! / Make!) |
| υ | ὑπάγω (bring forth)     | display x | Υ | display x as Unicode character |
| ς | σύμβολον (symbol/token) | N/A | Σ | N/A |


### Details, and modifications from Deadfish x:

* Reinstates the original Deadfish 'overflow' arithmetic behaviour (reset to 0 iff accumulator equals -1 OR 256). It is a feature, not a bug. Essential to allow values over 256 and enable the Unicode output required by ΙΧΘΥΣ.
* Output is Unicode, not ASCII.
* Does not refer to the definable 'functions' (The `X` command in Deadfish X, `Ι` in ΙΧΘΥΣ) as 'functions' since they take no arguments, return no results, and can only produce side-effects. In ΙΧΘΥΣ they are called 'statements', and have a number of important features, listed below.
* Adds a dedicated symbol (sigma) for labelling new statements.
* Statements are a collection of one or more statement symbols associated with a symbol, 'ς'.
* There is no execute command (Deadfish x `C`) required to trigger a defined statement, ΙΧΘΥΣ simply interprets the symbol if it can find a definition.
* Statement definitions can be nested.
* Statements definitions can be recursive.
* Statement symbols can be read before they are defined (or after they have been removed). There is no error on unrecognised symbols, simply a NOOP.
* Appying subsequent satement definitions (`Ι`) to an existing symbol *appends* to the statement definition, not overwrites.
* A statement definition is *removed* from storage if the Deadfish 'overflow' condition is triggered while reading from its definition. Only the symbol definition is removed, no action is taken with copies currently being read.
* Built-in command definitions are *not* appendable or removable, but they can be overwritten with new statement definitions that use the original command symbol.

### Architecture
* A counting board (abacus) and pebbles to track the tally. (accumulator: *x*)
* A large pithos (storage jar) to store inscribed ostraka (clay fragments)
* A stack of papyrus sheets to track current symbols (primary storage)
* A line in the sand creating two rows, (2 register stacks)
  * one above for a list of ostraka currently being read
  * the other below for a list of ostraka currently being written
* A magic fish that can manifest Unicode specification characters

**Other equipment:** A sharp point for inscribing ostraka, a reed pen and ink for transcribing to papyrus, a wooden stick for drawing σύμβολα in the sand, many blank potsherds, a pile of extra abacuses and stones (for `θ`), wine.

**Procedure:** The slave/scribe (δοῦλος) begins with a sheet of papyrus, already containing some symbols. 
 ... _TODO: expand this section_ ...
New statements are inscribed on ostraka, assigned a symbol (sigma) and placed in the pithos.

### Examples


```ΙΧΘΥΣ
ιιθιιιιθιιιιιιιιΥΧιιθιιιιιιθιΥιιιιιιιΥΥιιιΥΧιιιιιιιθχχχχχΥΧιιιιιιθχχχχΥΧιιιθιιθχχΥχχχχχχχχΥιιιΥχχχχχχΥχχχχχχχχΥΧιιιιιιθχχχΥ
```
"Hello, World!" (direct port from the Deadfish x version)
**OUTPUT:** `Hello, world!`


```ΙΧΘΥΣ
ΙΣιΥΘιιθιιιιθΣΣΣΣΣΣΣΣΣΣΣΣΣΣΣΣΣΣΣΣΣΣΣΣΣΣ
```
Alphabet (Latin), again ported, but compressed, from Deadfish x example:
**OUTPUT:** `ABCDEFGHIJKLMNOPQRSTUVWXYZ`


```ΙΧΘΥΣ
XΙΣιΥΘιιιιιθιιιιιθιιιιιιιιιιιιΣΣΣΣΣΣΣΣΣΣΣΣΣΣΣΣΣιΣΣΣΣΣΣΣ

```
With its Unicode support, ΙΧΘΥΣ can just as easily display the Greek alphabet
**OUTPUT:** `ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ`


```ΙΧΘΥΣ
ΧΙΣιΥΘΙσχχχχχχχχχχχχχχχχχχχχχχχχχχχχΘιιιθιιιιιιιιθσθχχσσσσσσσσσσΣΣΣΣΣΣΣΣΣΣΣΣΣΣΣΣΣΣΣΣΣΣ
```
And is not limted to just Greek, but can output from any Unicode block, for example, in Phoenician:
**OUTPUT:** `𐤀𐤁𐤂𐤃𐤄𐤅𐤆𐤇𐤈𐤉𐤊𐤋𐤌𐤍𐤎𐤏𐤐𐤑𐤒𐤓𐤔𐤕`

#### Non-Latin charset "Hello World"s
A more representative example for ΙΧΘΥΣ is to print 'Hello World' in Classical Greek:
```ΙΧΘΥΣ
ΙΣΧιιιιιθιιιιιιθΘΙϛχχχχχχχΘΙσϛϛιΘΙϲιιιιιιιιΘΣσσΥϲιιΥϲΥϲΥισΥΧιιθιιθϲΥΣσσσΥϲϲϲϲϲχχχΥιιιιΥϛΥϛΥΧιιιιιθϲΥ
```
**OUTPUT:** `Χαιρε,Κοσμε!`

#### Deadfish interpreter in ΙΧΘΥΣ
Since ΙΧΘΥΣ is a superset of Deadfish, it is relatively trivial to create a compliant Deadfish interpreter, e.g. for standard "idso" version:
```ΙΧΘΥΣ
ΙiιΘΙdχΘΙsθΘΙoυΘΧ

```

### File Extension
The official file extension for ΙΧΘΥΣ code is `.ἰχ`, U+1F30 U+03C7, not to be confused with the letters `ix`.

### The SYNTAX ERROR
There is only one form of syntax error in ΙΧΘΥΣ.
Any line terminated with a sigma / σύμβολον character that is not a final-form sigma will result in a **SYNTAX ERROR**.
On encountering  such a **SYNTAX ERROR**, it may be challenged by an argument referencing at least one *published* academic article from the
fields of classical studies, epigraphy, philology, or even less plausibly, computer science etc.

This does not mean lines _have_ to end in a sigma, simply that if they do, they must be of an appropriate final form.

**valid**
```ΙΧΘΥΣ
>> ΙΣιιιυΘΣ
3
```

```ΙΧΘΥΣ
>> ΙςιιιυΘς
3
```

**invalid**
```ΙΧΘΥΣ
>> ΙσιιιυΘσ
SYNTAX ERROR
```

### The Non-Aristotelian Syllogism

* All Unicode code points can be represented by ΙΧΘΥΣ, except Ā, Latin Capital Letter A With Macron (U+0100).
* Ā, 'Null-A', refers to non-Aristotelian logic. [¹](https://en.wikipedia.org/wiki/The_World_of_Null-A#Non-Aristotelian%20logic)
* Therefore, ΙΧΘΥΣ cannot represent non-Aristotelian logic.

### Localisation

### Computational Class

