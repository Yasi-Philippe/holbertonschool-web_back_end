# Node JS Basics

## Description

Introduction to Node.js fundamentals: running JavaScript on the server, handling I/O, building HTTP servers with Node's built-in `http` module and with Express, and organizing a full server using ES6 modules with Babel.

## Requirements

- Node.js 12.x
- npm

## Installation

```bash
npm install
```

## Tasks

### 0. Executing basic javascript with Node JS

**File:** `0-console.js`

Exports a `displayMessage` function that prints a string to STDOUT.

```bash
node 0-main.js
# Hello NodeJS!
```

---

### 1. Using Process stdin

**File:** `1-stdin.js`

A command-line program that prompts the user for their name and prints it back. Displays a closing message when the input stream ends.

```bash
node 1-stdin.js
# Welcome to Holberton School, what is your name?

echo "John" | node 1-stdin.js
# Welcome to Holberton School, what is your name?
# Your name is: John
# This important software is now closing
```

---

### 2. Reading a file synchronously with Node JS

**File:** `2-read_file.js`

Exports a `countStudents` function that synchronously reads a CSV database and logs the total number of students and a breakdown per field.

```bash
node 2-main_1.js
# Number of students: 10
# Number of students in CS: 6. List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie
# Number of students in SWE: 4. List: Guillaume, Joseph, Paul, Tommy
```

Throws `Error: Cannot load the database` if the file is not found.

---

### 3. Reading a file asynchronously with Node JS

**File:** `3-read_file_async.js`

Same as task 2 but the `countStudents` function is asynchronous and returns a Promise, keeping the event loop unblocked.

```bash
node 3-main_1.js
# After!
# Number of students: 10
# Number of students in CS: 6. List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie
# Number of students in SWE: 4. List: Guillaume, Joseph, Paul, Tommy
# Done!
```

---

### 4. Create a small HTTP server using Node's HTTP module

**File:** `4-http.js`

An HTTP server listening on port **1245** that responds with `Hello Holberton School!` as plain text for any endpoint.

```bash
curl localhost:1245
# Hello Holberton School!
```

---

### 5. Create a more complex HTTP server using Node's HTTP module

**File:** `5-http.js`

HTTP server on port **1245** with two routes:

| Route | Response |
|-------|----------|
| `/` | `Hello Holberton School!` |
| `/students` | Student list read from the CSV passed as a CLI argument |

```bash
node 5-http.js database.csv
curl localhost:1245/students
# This is the list of our students
# Number of students: 10
# ...
```

---

### 6. Create a small HTTP server using Express

**File:** `6-http_express.js`

Express server on port **1245** that handles `GET /` and returns `Hello Holberton School!`. All other routes return Express's default 404 page.

```bash
node 6-http_express.js
curl localhost:1245
# Hello Holberton School!
```

---

### 7. Create a more complex HTTP server using Express

**File:** `7-http_express.js`

Express server on port **1245** with the same routing as task 5 but built with Express.

```bash
node 7-http_express.js database.csv
curl localhost:1245/students
# This is the list of our students
# ...
```

---

### 8. Organize a complex HTTP server using Express

A full Express server structured into controllers, routes, and utilities using ES6 `import/export` syntax transpiled by Babel.

**Directory structure:**

```
full_server/
├── controllers/
│   ├── AppController.js
│   └── StudentsController.js
├── routes/
│   └── index.js
├── server.js
└── utils.js
```

**Files:**

- `full_server/utils.js` — `readDatabase(filePath)`: reads the CSV asynchronously and returns a Promise resolving to an object of student arrays keyed by field.
- `full_server/controllers/AppController.js` — `getHomepage`: returns `Hello Holberton School!`.
- `full_server/controllers/StudentsController.js`:
  - `getAllStudents`: returns the full student list sorted alphabetically by field.
  - `getAllStudentsByMajor`: accepts a `:major` param (`CS` or `SWE`) and returns the list for that field. Returns 500 for any other value.
- `full_server/routes/index.js` — Wires `/`, `/students`, and `/students/:major` to their controllers.
- `full_server/server.js` — Creates and exports the Express app listening on port **1245**.

**Run:**

```bash
npm run dev
```

```bash
curl localhost:1245
# Hello Holberton School!

curl localhost:1245/students
# This is the list of our students
# Number of students in CS: 6. List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie
# Number of students in SWE: 4. List: Guillaume, Joseph, Paul, Tommy

curl localhost:1245/students/SWE
# List: Guillaume, Joseph, Paul, Tommy

curl localhost:1245/students/French
# Major parameter must be CS or SWE
```

---

## Repository

- **GitHub:** holbertonschool-web_back_end
- **Directory:** Node_JS_basic
