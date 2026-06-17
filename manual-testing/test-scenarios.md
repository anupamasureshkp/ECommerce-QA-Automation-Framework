# Test Scenarios

## Registration & Login

| Scenario ID | Test Scenario | Priority |
|---|---|---|
| TS-001 | Verify user can register with valid details | High |
| TS-002 | Verify user cannot register with an already registered email address | High |
| TS-003 | Verify mandatory fields are validated during registration | High |
| TS-004 | Verify user can login with valid email and password | High |
| TS-005 | Verify user cannot login with invalid password | High |
| TS-006 | Verify user can logout successfully | Medium |

## Product Search & Product Details

| Scenario ID | Test Scenario | Priority |
|---|---|---|
| TS-007 | Verify user can search for an existing product | High |
| TS-008 | Verify system handles search with non-existing product keyword | Medium |
| TS-009 | Verify system handles search using special characters | Medium |
| TS-010 | Verify product details page displays correct product information | Medium |

## Cart Management

| Scenario ID | Test Scenario | Priority |
|---|---|---|
| TS-011 | Verify user can add a product to cart | High |
| TS-012 | Verify user can remove a product from cart | High |
| TS-013 | Verify cart quantity can be updated correctly | High |
| TS-014 | Verify cart total updates correctly after quantity change | High |
| TS-015 | Verify cart becomes empty after removing all products | Medium |

## Checkout Flow

| Scenario ID | Test Scenario | Priority |
|---|---|---|
| TS-016 | Verify registered user can proceed to checkout | High |
| TS-017 | Verify order summary displays correct product and price details | High |
| TS-018 | Verify user can place an order with valid payment details | High |
| TS-019 | Verify checkout flow prevents incomplete required fields | High |

## Contact Form

| Scenario ID | Test Scenario | Priority |
|---|---|---|
| TS-020 | Verify user can submit contact form with valid details | Medium |
| TS-021 | Verify contact form validates mandatory fields | Medium |
| TS-022 | Verify file upload option works in contact form | Low |

## Subscription & Account Deletion

| Scenario ID | Test Scenario | Priority |
|---|---|---|
| TS-023 | Verify user can subscribe using a valid email address | Low |
| TS-024 | Verify subscription handles invalid email format | Low |
| TS-025 | Verify logged-in user can delete account successfully | Medium |
