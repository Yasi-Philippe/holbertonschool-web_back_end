# ES6 Data Manipulation

A JavaScript project exploring ES6 data structures and array manipulation methods, built with Node.js 20.x, Jest, Babel, and ESLint.

## Requirements

- Node.js 20.x.x / npm 9.x.x
- All files use the `.js` extension
- Code tested with Jest (`npm run test`)
- Linting enforced with ESLint (`npm run full-test`)
- All functions are exported

## Setup

Install dependencies after cloning:

```bash
npm install
```

## Scripts

| Command | Description |
|---|---|
| `npm run dev <file>` | Run a file with Babel |
| `npm run test` | Run Jest tests |
| `npm run lint` | Run ESLint |
| `npm run full-test` | Lint + tests |

## Functions

### `getListStudents` — [0-get_list_students.js](0-get_list_students.js)

Returns a hardcoded array of student objects, each with `id` (Number), `firstName` (String), and `location` (String).

### `getListStudentIds` — [1-get_list_student_ids.js](1-get_list_student_ids.js)

Accepts an array of student objects and returns an array of their `id` values using `map`. Returns an empty array if the argument is not an array.

### `getStudentsByLocation` — [2-get_students_by_loc.js](2-get_students_by_loc.js)

Accepts a student list and a city string, returns only the students located in that city using `filter`.

### `getStudentIdsSum` — [3-get_ids_sum.js](3-get_ids_sum.js)

Accepts a student list and returns the sum of all student `id` values using `reduce`.

### `updateStudentGradeByCity` — [4-update_grade_by_city.js](4-update_grade_by_city.js)

Accepts a student list, a city, and an array of grade objects `{ studentId, grade }`. Returns students from that city with their grade appended. Students without a matching grade entry receive `'N/A'`. Uses `filter` and `map`.

### `createInt8TypedArray` — [5-typed_arrays.js](5-typed_arrays.js)

Accepts `length`, `position`, and `value`. Creates an `ArrayBuffer` of the given length, writes an `Int8` value at the given position via `DataView`, and returns the view. Throws `Position outside range` if the position is invalid.

### `setFromArray` — [6-set.js](6-set.js)

Accepts an array of any elements and returns a `Set` built from it.

### `hasValuesFromArray` — [7-has_array_values.js](7-has_array_values.js)

Accepts a `Set` and an array, returns `true` if every element in the array exists in the set, `false` otherwise.

### `cleanSet` — [8-clean_set.js](8-clean_set.js)

Accepts a `Set` and a `startString`. Returns a `-`-separated string of the suffixes of all set values that begin with `startString`. Returns an empty string if `startString` is empty or not a string.

### `groceriesList` — [9-groceries_list.js](9-groceries_list.js)

Returns a `Map` of grocery items with their quantities: Apples (10), Tomatoes (10), Pasta (1), Rice (1), Banana (5).

### `updateUniqueItems` — [10-update_uniq_items.js](10-update_uniq_items.js)

Accepts a `Map` and updates every entry whose quantity is `1` to `100`. Throws `Cannot process` if the argument is not a `Map`.
