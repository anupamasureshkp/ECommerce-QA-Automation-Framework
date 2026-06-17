# Defect Reports

## Execution Summary

| Test Case ID | Module                          | Status |
| ------------ | ------------------------------- | ------ |
| TC-001       | Registration with valid details | Pass   |
| TC-002       | Existing email registration     | Pass   |
| TC-003       | Mandatory field validation      | Pass   |
| TC-004       | Valid email format              | Pass   |
| TC-005       | Invalid email format            | Pass   |

---

## BUG-001 - Password field accepts weak password without validation message

**Module:** Registration
**Severity:** Medium
**Priority:** Medium
**Environment:** Windows 11, Google Chrome

### Steps to Reproduce

1. Navigate to Signup/Login page.
2. Enter valid name and email.
3. Complete registration form.
4. Enter a very short password, such as `a`.
5. Submit the form.

### Expected Result

System should enforce password rules such as minimum length, maximum length and/or complexity, and display a clear validation message.

### Actual Result

System accepts any password value as long as something is entered.

### Status

Open

---

## BUG-002 - Postcode field accepts invalid format

**Module:** Registration
**Severity:** Medium
**Priority:** Medium
**Environment:** Windows 11, Google Chrome

### Steps to Reproduce

1. Navigate to Signup/Login page.
2. Enter valid name and email.
3. Complete the registration form.
4. Enter invalid postcode value, such as `abcxyz` or random characters.
5. Submit the form.

### Expected Result

Postcode field should validate the entered value based on an accepted postcode/zip code format.

### Actual Result

System accepts invalid postcode values without validation.

### Status

Open

---

## BUG-003 - Mobile number field accepts alphabetic and special character input

**Module:** Registration
**Severity:** Medium
**Priority:** High
**Environment:** Windows 11, Google Chrome

### Steps to Reproduce

1. Navigate to Signup/Login page.
2. Enter valid name and email.
3. Complete the registration form.
4. Enter alphabetic or special characters in the mobile number field.
5. Submit the form.

### Expected Result

Mobile number field should accept only valid numeric input and display an error message for invalid characters.

### Actual Result

Mobile number field accepts letters and non-numeric characters.

### Status

Open

---

## Observation-001 - Country dropdown has limited selectable options

**Module:** Registration
**Severity:** Low
**Priority:** Low

### Observation

The country dropdown provides only a limited number of country options.

### Impact

Users from unsupported countries may not be able to select their correct country during registration.

### Recommendation

Expand the country list or provide a more complete country selection option.
