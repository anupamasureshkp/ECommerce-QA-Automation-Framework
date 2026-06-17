# Risk Matrix

| Module                  | Risk Level | Priority | Reason                                             |
| ----------------------- | ---------- | -------- | -------------------------------------------------- |
| User Registration       | High       | High     | Users must be able to create accounts successfully |
| Login / Authentication  | High       | High     | Core functionality required for user access        |
| Product Search          | Medium     | Medium   | Impacts user experience and product discovery      |
| Product Details         | Medium     | Medium   | Incorrect information may affect purchases         |
| Cart Management         | High       | High     | Incorrect cart behaviour can lead to order issues  |
| Checkout Process        | High       | High     | Revenue-impacting functionality                    |
| Contact Us Form         | Low        | Low      | Secondary business functionality                   |
| Newsletter Subscription | Low        | Low      | Non-critical feature                               |
| Account Deletion        | Medium     | Medium   | User data management functionality                 |

---

## High Risk Areas

* Login and Authentication
* Cart Calculations
* Checkout Flow
* User Registration

## Medium Risk Areas

* Product Search
* Product Details
* Account Deletion

## Low Risk Areas

* Contact Form
* Newsletter Subscription

## Risk Mitigation Strategy

* Prioritize testing of high-risk modules.
* Execute regression tests for critical workflows.
* Automate repetitive and high-value test scenarios.
* Record and track defects with severity and priority classifications.
