# Running tests

First, fix the URL in `playwright.config.ts`.

Then run:

```
$ npm install
$ npx playwright install chromium
$ npx playwright test --headed
```

Note: feel free to remove the `slowMo` option in the test when you're not debugging.