### 4. **Delete:**

**Command:** Delete the book you created and confirm the deletion by trying to retrieve all books again.

**Documentation File:** `delete.md`

```markdown
# Delete the Book Instance

```python
# Delete the book instance
retrieved_book.delete()

# Confirm deletion by retrieving all books
all_books = Book.objects.all()
print(list(all_books))  # Expected output: Empty list `[]`
