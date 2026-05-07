# ES6 Promises

A JavaScript project covering Promise creation, chaining, error handling, and concurrent resolution using ES6+ syntax. Built with Node.js 20.x, Jest, Babel, and ESLint.

## Requirements

- Node.js 20.x.x / npm 9.x.x
- All files use the `.js` extension
- Code tested with Jest (`npm run test`)
- Linting enforced with ESLint (`npm run full-test`)
- All functions are exported

## Setup

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

### `getResponseFromAPI` — [0-promise.js](0-promise.js)

Returns a `Promise` instance.

### `getFullResponseFromAPI` — [1-promise.js](1-promise.js)

Accepts a boolean `success`. Resolves with `{ status: 200, body: 'Success' }` when `true`, rejects with an `Error` when `false`.

### `handleResponseFromAPI` — [2-then.js](2-then.js)

Accepts a promise and appends handlers: resolves to `{ status: 200, body: 'success' }`, rejects to an empty `Error`, and logs `Got a response from the API` on every resolution via `finally`.

### `handleProfileSignup` — [3-all.js](3-all.js)

Resolves `uploadPhoto` and `createUser` from `utils.js` concurrently with `Promise.all` and logs `body firstName lastName`. Logs `Signup system offline` on failure.

### `signUpUser` — [4-user-promise.js](4-user-promise.js)

Accepts `firstName` and `lastName`, returns a resolved promise with `{ firstName, lastName }`.

### `uploadPhoto` — [5-photo-reject.js](5-photo-reject.js)

Accepts a `filename` string, returns a rejected promise with an `Error` stating `<filename> cannot be processed`.

### `handleProfileSignup` — [6-final-user.js](6-final-user.js)

Accepts `firstName`, `lastName`, and `fileName`. Calls `signUpUser` and `uploadPhoto` concurrently via `Promise.allSettled` and returns an array of `{ status, value }` objects for each settled promise.

### `loadBalancer` — [7-load_balancer.js](7-load_balancer.js)

Accepts two promises (`chinaDownload`, `USDownload`) and returns the value of whichever resolves first using `Promise.race`.

### `divideFunction` — [8-try.js](8-try.js)

Accepts `numerator` and `denominator`. Returns the division result, or throws `Error: cannot divide by 0` when the denominator is `0`.

### `guardrail` — [9-try.js](9-try.js)

Accepts a `mathFunction`. Executes it inside a `try/catch/finally` block, appends either the return value or the error message to a `queue` array, then always appends `'Guardrail was processed'`. Returns the queue.
