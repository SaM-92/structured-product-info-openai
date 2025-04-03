import os
from openai import OpenAI
from pydantic import BaseModel  # Standard import

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o-mini"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

class Product(BaseModel):  # Using standard Pydantic import
    id: str
    name: str
    price: float
    category: str
    in_stock: bool

completion = client.beta.chat.completions.parse(
    model=model_name,
    messages=[
        {"role": "system", "content": "You extract product information into structured data."},
        {"role": "user", "content": "Extract: The XPS 13 laptop costs $999 and is in the premium category. Currently in stock."},
    ],
    response_format=Product,
)

message = completion.choices[0].message
if message.parsed:
    product = message.parsed
    
    # Print in database-friendly format
    print(f"Database record ready for insertion:")
    print(f"Product : {product}")

    # Example of how you'd prepare for SQL
    print("\nSQL example:")
    print(f"INSERT INTO products VALUES ('{product.id}', '{product.name}', {product.price}, '{product.category}', {product.in_stock});")
else:
    print(message.refusal)
