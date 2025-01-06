import { test, expect, chromium } from '@playwright/test'

test('has title', async () => {
  const browser = await chromium.launch({ slowMo: 1000 })
  const page = await browser.newPage()

  // Reset database
  await page.goto('/reset_db')
  const proceedButton = page.locator("button:has-text('proceed')")
  await proceedButton.click()

  // Create a new team
  await page.goto('/add_team')
  const nameInput = page.locator('input[name="name"]')
  const team_name = 'my team'
  await nameInput.fill(team_name)
  await page.click("text='Add'")

  // Check the team has been created
  await page.goto("/teams")
  await page.isVisible(`td:has-text('${team_name}')`)
})
