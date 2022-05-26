# pytest-pcpress

In this project, the web page being tested is "Prodavnica" page of the pcpress.rs site.
URL: https://pcpress.rs/prodavnica/index.php/
Program executes positive test cases and negative test cases, based on documentation.
PyTest tool is used to create test framework, and Selenium WebDriver is used to manage web page elements.
Page Object Model is used as a design pattern. Under the Page Object Model, page classes are created for all the webpages that are a part of the Automation Under Test. Test data is read from a CSV file.
Full testing documentation for the specified page is also uploaded in manualqa-pcpress directory.

Future plans are to improve programs functionalities, add test cases for links, etc.
Program is built to be modular, so adding new test cases should be simple task.