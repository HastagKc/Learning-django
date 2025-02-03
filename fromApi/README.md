# Django's **Form API**

Django's **Form API** provides a structured way to handle **HTML forms**, including validation, rendering, and processing user input. It simplifies form handling by automatically generating form fields, handling errors, and integrating with Django's model system.

---

## **📌 Why Use Django Forms?**

- **Automatic Form Generation** – No need to manually write HTML form fields.
- **Built-in Validation** – Ensures correct data input before saving.
- **Security** – Protects against CSRF attacks and malicious data.
- **Easier Handling** – Django automatically converts submitted data into Python objects.

---

## **📌 How to Use Django Forms**

### **1️⃣ Define a Form Class**

Django forms are created as Python classes that inherit from `forms.Form` (for non-model forms) or `forms.ModelForm` (for forms linked to models).

🔹 **Example: Basic Form**

```python
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

```

This creates a **contact form** with three fields: **name, email, and message**.

---

### **2️⃣ Use the Form in a View**

You need to **instantiate the form** in a Django view and send it to a template.

🔹 **Example: Rendering the Form in a View**

```python
from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    form = ContactForm()
    return render(request, "contact.html", {"form": form})

```

---

### **3️⃣ Display the Form in a Template**

You can use Django’s form rendering methods in your template.

🔹 **Example: Simple Form Rendering**

```html
<form method="post">
  {% csrf_token %} {{ form.as_p }}
  <button type="submit">Submit</button>
</form>
```

✔ `{{ form.as_p }}` automatically generates labeled fields wrapped in `<p>` tags.

---

### **4️⃣ Handling Form Submission**

When the user submits the form, you need to **validate and process the data**.

🔹 **Example: Processing Form Data in a View**

```python
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data (e.g., save to database or send email)
            print(form.cleaned_data)
    else:
        form = ContactForm()
    return render(request, "contact.html", {"form": form})

```

✔ `form.is_valid()` checks if the form data is correct.

✔ `form.cleaned_data` provides a dictionary of validated data.

---

## **📌 Summary**

- Define a form using `forms.Form`
- Use the form in a Django view
- Render the form in an HTML template
- Handle form submission and validation

## id, label, initial and field-order Customization

---

Django’s `forms.Form` provides a powerful way to create and manage **HTML forms** in Python. This documentation explains how to customize forms with **auto_id, label_suffix, field order, and initial values**.

---

## **📌 1. Creating a Form**

A Django form is defined by subclassing `forms.Form` and specifying fields.

### **🔹 Example: Basic Form**

```python
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

```

✔ This creates a form with **name, email, and message fields**.

---

## **📌 2. `auto_id`: Customizing HTML ID Attributes**

Django assigns **default `id` attributes** to form fields. The `auto_id` parameter customizes these.

### **✅ `auto_id` Options**

| **Value**        | **Effect**                                    |
| ---------------- | --------------------------------------------- |
| `True` (default) | Uses `id_<field_name>` (e.g., `id_email`)     |
| `False`          | Removes `id` attributes                       |
| `"prefix_%s"`    | Uses `prefix_<field_name>` (e.g., `kc_email`) |
| `"prefix"`       | Same as `True` (default behavior)             |

### **🔹 Example: Setting `auto_id`**

```python
form = ContactForm(auto_id="kc_%s")

```

🔹 **Generated HTML Output:**

```html
<label for="kc_email">Email:</label>
<input type="email" name="email" id="kc_email" />
```

If `auto_id=False`:

```html
<input type="email" name="email" />
```

✔ No `id` attribute is generated.

---

## **📌 3. `label_suffix`: Customizing Field Labels**

Django **automatically adds a colon (`:`) at the end of labels**. You can change or remove this using `label_suffix`.

### **🔹 Example: Custom `label_suffix`**

```python
form = ContactForm(label_suffix=" *")

```

✔ **Now labels will render as:**

```html
<label for="id_email">Email *</label>
<input type="email" name="email" id="id_email" />
```

✔ **To remove the suffix:**

```python
form = ContactForm(label_suffix="")

```

🔹 Labels will now appear without any suffix.

---

## **📌 4. `field_order`: Changing Field Display Order**

By default, Django **renders fields in the order they are defined**. You can override this with `field_order`.

### **🔹 Example: Reordering Fields**

```python
class CustomForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        field_order = ["email", "first_name", "last_name"]

```

✔ **Rendered Order:**
1️⃣ **Email**

2️⃣ **First Name**

3️⃣ **Last Name**

Alternatively, you can specify `field_order` in the **view**:

```python
form = CustomForm(field_order=["last_name", "email", "first_name"])

```

---

## **📌 5. `initial`: Setting Default Field Values**

Django allows **prepopulating fields with default values** using `initial`.

### **🔹 Example: Default Values**

```python
class CustomForm(forms.Form):
    name = forms.CharField(initial="John Doe")
    email = forms.EmailField(initial="john@example.com")

```

✔ **Rendered HTML Output:**

```html
<input type="text" name="name" value="John Doe" />
<input type="email" name="email" value="john@example.com" />
```

✔ You can also **override `initial` dynamically** in the view:

```python
form = CustomForm(initial={"name": "Alice", "email": "alice@example.com"})

```

✔ The form will now have:

- **Name:** Alice
- **Email:** [alice@example.com](mailto:alice@example.com)

---

## **📌 6. Full Example: Custom Form with `auto_id`, `label_suffix`, `field_order`, and `initial`**

```python
class CustomForm(forms.Form):
    first_name = forms.CharField(label="First Name", initial="John")
    last_name = forms.CharField(label="Last Name", initial="Doe")
    email = forms.EmailField(label="Email Address", initial="john.doe@example.com")

    class Meta:
        auto_id = "kc_%s"  # Custom ID format
        label_suffix = " *"  # Custom label suffix
        field_order = ["email", "first_name", "last_name"]  # Custom field order

```

✔ **Rendered HTML Output:**

```html
<label for="kc_email">Email Address *</label>
<input type="email" name="email" id="kc_email" value="john.doe@example.com" />

<label for="kc_first_name">First Name *</label>
<input type="text" name="first_name" id="kc_first_name" value="John" />

<label for="kc_last_name">Last Name *</label>
<input type="text" name="last_name" id="kc_last_name" value="Doe" />
```

---

## **📌 Conclusion**

| **Feature**    | **Purpose**                           | **Usage Example**                                      |
| -------------- | ------------------------------------- | ------------------------------------------------------ |
| `auto_id`      | Customizes field ID attributes        | `form = CustomForm(auto_id="kc_%s")`                   |
| `label_suffix` | Changes or removes label suffix       | `form = CustomForm(label_suffix=" *")`                 |
| `field_order`  | Changes the order of displayed fields | `class Meta: field_order = ["email", "first_name"]`    |
| `initial`      | Sets default field values             | `email = forms.EmailField(initial="user@example.com")` |

---

### **🔹 Summary**

✔ **`auto_id`** customizes field **IDs**

✔ **`label_suffix`** customizes the **label ending**

✔ **`field_order`** allows reordering **form fields**

✔ **`initial`** sets **default values**
