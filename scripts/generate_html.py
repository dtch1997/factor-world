""" Generate the HTML file that shows the factors of variation """

from factorworld.envs import list_factors

gif_names = list_factors()

# Generate the HTML dynamically
html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GIF Grid</title>
    <style>
        /* Style the container div */
        .gif-container {
            display: grid;
            grid-template-columns: repeat(3, 1fr); /* Adjust the number of columns as needed */
            gap: 20px; /* Adjust the gap between items */
        }

        /* Style each individual gif item */
        .gif-item {
            text-align: center;
        }

        .gif-item img {
            max-width: 100%; /* Adjust the maximum width as needed */
            max-height: 300px; /* Adjust the maximum height as needed */
        }
    </style>
</head>
<body>
    <div class="gif-container">
"""

for gif_name in gif_names:
    html += f"""
        <!-- GIF with label for {gif_name} -->
        <div class="gif-item">
            <img src="assets/{gif_name}.gif" alt="{gif_name}">
            <p>{gif_name}</p>
        </div>
    """

html += """
    </div>
</body>
</html>
"""

# Save the generated HTML to a file
with open("docs/factors.html", "w") as output_file:
    output_file.write(html)
