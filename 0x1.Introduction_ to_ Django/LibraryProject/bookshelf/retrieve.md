### 2. **Retrieve:**

**Command:** Retrieve and display all attributes of the book you just created.

**Documentation File:** `retrieve.md`

```markdown
# Retrieve the Book Instance

```python
# Retrieve the book instance by ID
retrieved_book = Book.objects.get(id=1)

# Display all attributes of the book
print(f"Title: {retrieved_book.title}")
print(f"Author: {retrieved_book.author}")
print(f"Published Date: {retrieved_book.published_date}")
