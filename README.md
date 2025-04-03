# 🤖 GitHub Models - Structured Output Example

This repository demonstrates OpenAI's Structured Output feature using GitHub Models. This feature is a game-changer for developers because:
- 🎯 It eliminates the need for complex parsing of AI responses
- 🔒 Guarantees type-safe data structures
- 🚀 Reduces errors and validation code

## ✨ Why Structured Outputs?
Instead of getting raw text and parsing it yourself, the API returns data in exactly the structure you need. Imagine getting JSON-like responses that are automatically validated and converted to your programming language's native types!

## 🛠 About Pydantic
Pydantic is the engine behind our data validation:
- Automatically converts and validates data types
- Provides clear error messages if data doesn't match expected format
- Works seamlessly with Python type hints

## 💡 Example Explained
```python
# This is what happens in our code:
1. We define a Product model with specific fields (id, name, price, etc.)
2. The API extracts info from natural text: "The XPS 13 laptop costs $999..."
3. Returns a perfectly structured object, ready for database insertion!
```

## 🚀 Quick Start

1. Open in Codespace
2. Ensure `GITHUB_TOKEN` is set in your environment
3. Run the example:
```bash
python product_extractor.py
```

## 📝 Example Output
```python
Database record ready for insertion:
Product: {
    "id": "xps13",
    "name": "XPS 13 laptop",
    "price": 999.0,
    "category": "premium",
    "in_stock": true
}

SQL example:
INSERT INTO products VALUES ('xps13', 'XPS 13 laptop', 999.0, 'premium', true);
```

## ⚠️ Important Notes
- This is a beta feature with usage limits
- Uses Azure AI Content Safety filters
- See [Pre-release Terms](https://docs.github.com/en/site-policy/github-terms/github-pre-release-license-terms) for details
