
### Getting Started with CSS:

1. **Introduction to Inline, Internal, and External CSS:**

Exercise: Apply inline, internal, and external styles to the same HTML document to change the color of a paragraph.

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        /* Internal Style */
        p {
            color: blue;
        }
    </style>
</head>
<body>
    <p style="color: red;">This is an inline style.</p>
    <p>This paragraph uses internal style.</p>
    <p>This is the default color.</p>
</body>
</html>
```

2. **Basic Syntax and Structure of CSS Rules:**

Exercise: Create a CSS rule to change the background color of an element with class "highlight".

```css
.highlight {
    background-color: yellow;
}
```

3. **Applying Styles to HTML Elements Using Selectors:**

Exercise: Apply styles to all `<h2>` elements using a selector.

```css
h2 {
    font-size: 24px;
    color: darkblue;
}
```

### CSS Selectors and Specificity:

1. **Overview of Different Types of Selectors:**

Exercise: Apply styles to all paragraphs within a `<div>` element with the ID "content".

```css
#content p {
    font-style: italic;
}
```

2. **Specificity and How the Browser Decides Styles:**

Exercise: Explain the outcome when a class selector and an ID selector target the same element.

Solution: The ID selector has higher specificity and will override the class selector's styles.

3. **Combining Selectors for Complex Targeting:**

Exercise: Apply styles to an anchor element with class "button" inside a `<div>` with class "container".

```css
.container .button {
    background-color: #007bff;
    color: white;
    padding: 10px 20px;
}
```

### Box Model and Layout:

1. **Understanding the Box Model:**

Exercise: Set different values for content, padding, border, and margin for a `<div>` element.

Solution: The following CSS styles create a colored box with different spacing:

```css
.box {
    width: 200px;
    height: 100px;
    padding: 20px;
    border: 2px solid black;
    margin: 10px;
    background-color: lightgray;
}
```

2. **Box-Sizing Property and Its Impact on Layout:**

Exercise: Create two boxes with different `box-sizing` values to observe the impact on layout.

```css
.box-content-box {
    width: 200px;
    height: 100px;
    padding: 20px;
    border: 2px solid black;
    margin: 10px;
    background-color: lightgray;
    box-sizing: content-box;
}

.box-border-box {
    width: 200px;
    height: 100px;
    padding: 20px;
    border: 2px solid black;
    margin: 10px;
    background-color: lightgray;
    box-sizing: border-box;
}
```

3. **Positioning and the Stacking Context:**

Exercise: Create an element with absolute positioning inside a relatively positioned container.

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        .container {
            position: relative;
            width: 300px;
            height: 300px;
        }

        .absolute-box {
            position: absolute;
            top: 50px;
            left: 50px;
            width: 150px;
            height: 150px;
            background-color: lightblue;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="absolute-box"></div>
    </div>
</body>
</html>
```

### Typography and Text Styling:

1. **Font Properties:**

Exercise: Apply different font properties to a heading element.

```css
h1 {
    font-family: Arial, sans-serif;
    font-size: 36px;
    font-weight: bold;
    font-style: italic;
}
```

2. **Text Color, Alignment, and Decoration:**

Exercise: Style an anchor element to have a specific color, text alignment, and no underlining.

```css
a {
    color: #007bff;
    text-align: center;
    text-decoration: none;
}
```

3. **Line Height, Letter Spacing, and Text Shadows:**

Exercise: Apply line height, letter spacing, and a text shadow to a paragraph.

```css
p {
    line-height: 1.5;
    letter-spacing: 1px;
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
}
```

### Colors and Backgrounds:

1. **Using Named Colors, Hexadecimal, RGB, and HSL Values:**

Exercise: Apply different color values to elements using named colors, hexadecimal, RGB, and HSL values.

```css
.named-color {
    color: red;
}

.hex-color {
    color: #336699;
}

.rgb-color {
    color: rgb(255, 0, 128);
}

.hsl-color {
    color: hsl(120, 100%, 50%);
}
```

2. **Background Properties:**

Exercise: Create a styled button with different background properties.

```css
.button {
    padding: 10px 20px;
    border: none;
    color: white;
}

.button-primary {
    background-color: #007bff;
}

.button-secondary {
    background-image: linear-gradient(to bottom, #ff9900, #ff3300);
    background-size: cover;
}

.button-icon {
    background-image: url('icon.png');
    background-repeat: no-repeat;
    background-position: center;
    background-size: 20px 20px;
}
```

3. **Creating Gradients and Patterns:**

Exercise: Apply a linear gradient and a background pattern to different elements.

```css
.linear-gradient {
    background: linear-gradient(to bottom, #ff9900, #ff3300);
}

.pattern {
    background-image: url('pattern.png');
    background-repeat: repeat;
}
```

### Flexbox and Grid Layout:

1. **Introduction to Flexbox for One-Dimensional Layouts:**

Exercise: Create a simple row layout using Flexbox.

```css
.container {
    display: flex;
    justify-content: space-between;
    align-items: center;
}
```

2. **Creating Flexible and Responsive Layouts with Flexbox:**

Exercise: Create a centered and responsive navigation menu using Flexbox.

```css
.nav {
    display: flex;
    justify-content: center;
    background-color: lightgray;
    padding: 10px 0;
}

.nav-item {
    margin: 0 10px;
}
```

3. **Introduction to Grid Layout for Two-Dimensional Layouts:**

Exercise: Create a 2x2 grid layout using Grid.

```css
.grid-container {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    grid-template-rows: repeat(2

, 200px);
    gap: 10px;
}
```

4. **Building Complex Layouts Using Grid:**

Exercise: Create a responsive grid layout with header, sidebar, and main content.

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        .container {
            display: grid;
            grid-template-columns: 1fr 3fr;
            grid-gap: 20px;
            margin: 20px;
        }

        .sidebar {
            background-color: lightgray;
            padding: 10px;
        }

        .main-content {
            background-color: lightblue;
            padding: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="sidebar">
            Sidebar content
        </div>
        <div class="main-content">
            Main content
        </div>
    </div>
</body>
</html>
```

### Responsive Design:

1. **Media Queries and Responsive Breakpoints:**

Exercise: Apply media queries to adjust styles for different screen sizes.

```css
@media (max-width: 768px) {
    .responsive-element {
        font-size: 14px;
    }
}
```

2. **Creating Mobile-First and Desktop-First Designs:**

Exercise: Create a mobile-first layout with a navigation menu that transforms into a dropdown menu on smaller screens.

```css
@media (max-width: 768px) {
    .dropdown-menu {
        display: block;
    }

    .nav-item {
        display: none;
    }
}
```

3. **Flexibility and Fluidity in Responsive Layouts:**

Exercise: Create a flexible and fluid layout using Flexbox.

```css
.flex-container {
    display: flex;
    flex-wrap: wrap;
}

.flex-item {
    flex: 1;
    min-width: 200px;
    margin: 10px;
}
```

### Transitions and Animations:

1. **CSS Transitions for Smooth Property Changes:**

Exercise: Apply a smooth transition to a button's background color change.

```css
.button {
    background-color: #007bff;
    color: white;
    transition: background-color 0.3s ease-in-out;
}

.button:hover {
    background-color: #0056b3;
}
```

2. **Keyframe Animations for Creating Custom Animations:**

Exercise: Create a blinking animation using keyframes.

```css
@keyframes blink {
    0%, 100% {
        opacity: 1;
    }
    50% {
        opacity: 0;
    }
}

.blinking-element {
    animation: blink 1s infinite;
}
```

3. **Using Animation Properties and Timing Functions:**

Exercise: Apply a bounce animation to an element with a specific timing function.

```css
.bouncing-element {
    animation: bounce 0.5s cubic-bezier(0.68, -0.55, 0.27, 1.55) infinite alternate;
}

@keyframes bounce {
    0%, 100% {
        transform: translateY(0);
    }
    50% {
        transform: translateY(-20px);
    }
}
```

### Transforms and 3D Effects:

1. **Applying Transforms to Elements:**

Exercise: Apply different transforms to a `<div>` element.

```css
.transform-element {
    transform: translate(50px, 20px) rotate(45deg) scale(1.2) skew(10deg, 20deg);
}
```

2. **Creating 3D Effects with Perspective and Transform-Style:**

Exercise: Create a 3D card flip animation using perspective and transform-style.

```css
.card {
    width: 200px;
    height: 300px;
    transform-style: preserve-3d;
    transition: transform 0.5s;
}

.card:hover {
    transform: rotateY(180deg);
}
```

3. **Combining Transforms for Advanced Animations:**

Exercise: Create a rotating and scaling animation using combined transforms.

```css
@keyframes spin-and-scale {
    0% {
        transform: rotate(0) scale(1);
    }
    100% {
        transform: rotate(360deg) scale(1.5);
    }
}

.combined-animation {
    animation: spin-and-scale 3s linear infinite;
}
```

### Advanced Selectors and CSS3 Modules:

1. **Child and Sibling Selectors:**

Exercise: Style all immediate child elements of a parent element.

```css
.parent > .child {
    /* Styles applied to direct children */
}
```

2. **Attribute Selectors and Pseudo-Classes:**

Exercise: Apply styles to anchor elements with specific attributes.

```css
a[target="_blank"] {
    color: red;
}

input[type="text"]:focus {
    border-color: green;
}
```

3. **Introduction to CSS3 Modules:**

Exercise: Create a navigation bar using Flexbox from the Flexbox module.

```css
.nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
}
```

### CSS Preprocessors:

1. **Introduction to CSS Preprocessors:**

Exercise: Create a variable for primary color and use it in styling.

```scss
$

primary-color: #007bff;

.button {
    background-color: $primary-color;
}
```

2. **Using Variables, Mixins, and Nesting:**

Exercise: Create a mixin for centering elements and apply it to a div.

```scss
@mixin center-element {
    display: flex;
    justify-content: center;
    align-items: center;
}

.centered-box {
    @include center-element;
}
```

### CSS Frameworks:

1. **Overview of Popular CSS Frameworks:**

Exercise: Create a responsive navigation bar using Bootstrap classes.

```html
<nav class="navbar navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" href="#">Logo</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ml-auto">
            <li class="nav-item active">
                <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="#">Features</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="#">Pricing</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="#">Contact</a>
            </li>
        </ul>
    </div>
</nav>
```

2. **Using Frameworks to Expedite Development and Maintain Consistency:**

Exercise: Use Foundation's grid to create a responsive layout.

```html
<div class="grid-container">
    <div class="grid-x">
        <div class="cell small-6 medium-4 large-3">Column 1</div>
        <div class="cell small-6 medium-4 large-3">Column 2</div>
        <div class="cell small-12 medium-4 large-6">Column 3</div>
    </div>
</div>
```

