# ES6 Classes

A project exploring object-oriented programming in JavaScript using ES6 class syntax.

## Concepts covered

- Defining classes with constructors
- Private attributes (underscore convention)
- Getters and setters with type validation
- Class inheritance and `super`
- Abstract class pattern
- Static methods
- Overriding `Symbol.toStringTag` and `Symbol.toPrimitive`
- Fixing hoisting issues with classes
- Cloning instances using `this.constructor`

## Tasks

| File | Description |
|------|-------------|
| `0-classroom.js` | `ClassRoom` class storing `maxStudentsSize` |
| `1-make_classrooms.js` | Function returning an array of 3 `ClassRoom` instances |
| `2-hbtn_course.js` | `HolbertonCourse` class with type-checked getters and setters |
| `3-currency.js` | `Currency` class with `displayFullCurrency()` method |
| `4-pricing.js` | `Pricing` class with `displayFullPrice()` and static `convertPrice()` |
| `5-building.js` | Abstract `Building` class that enforces `evacuationWarningMessage` in subclasses |
| `6-sky_high.js` | `SkyHighBuilding` extending `Building` with `floors` and override |
| `7-airport.js` | `Airport` class using `Symbol.toStringTag` for custom string representation |
| `8-hbtn_class.js` | `HolbertonClass` using `Symbol.toPrimitive` for Number/String casting |
| `9-hoisting.js` | Fixed hoisting bugs: class declarations moved before usage, constructor and `this` corrections |
| `10-car.js` | `Car` class with `cloneCar()` that returns a new instance of the same class |

## Requirements

- Node.js 20.x
- Jest, Babel, ESLint (see `package.json`)

## Usage

```bash
npm run dev <file>      # run a file with babel-node
npm test                # run jest tests
npm run full-test       # lint + jest
```
