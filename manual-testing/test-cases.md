# Test Cases

## Registration Module

### TC-001 - Verify user can register with valid details

**Priority:** High

**Precondition:** User is not already registered.

**Test Data:** Valid name and unique email address.

**Steps:**

1. Navigate to Signup/Login page.
2. Enter valid name and email.
3. Click Signup.
4. Complete registration form.
5. Click Create Account.

**Expected Result:**
User account is created successfully and confirmation message is displayed.

---

### TC-002 - Verify registration with existing email address

**Priority:** High

**Precondition:** Email address already exists.

**Test Data:** Registered email address.

**Steps:**

1. Navigate to Signup/Login page.
2. Enter valid name.
3. Enter already registered email.
4. Click Signup.

**Expected Result:**
System displays appropriate error message and account is not created.

---

### TC-003 - Verify mandatory field validation during registration

**Priority:** High

**Steps:**

1. Navigate to Signup page.
2. Leave mandatory fields blank.
3. Attempt registration.

**Expected Result:**
Validation messages are displayed for required fields.

---

### TC-004 - Verify email field accepts valid email format

**Priority:** Medium

**Test Data:** [test@example.com](mailto:test@example.com)

**Steps:**

1. Enter valid email address.
2. Continue registration process.

**Expected Result:**
System accepts email address.

---

### TC-005 - Verify invalid email format is rejected

**Priority:** Medium

**Test Data:** testexample.com

**Steps:**

1. Enter invalid email format.
2. Attempt registration.

**Expected Result:**
System displays validation error.

