# Our goal:

Editing .epubs so they look like this:

![F4atKe5bkAEiBxr](https://github.com/Maidervierte/epubbold/assets/68083029/04f089bf-519a-4f4e-99a6-e8259bdde8bc)

# Usage instructions

## Step 1

[Download the most recent release.](https://github.com/Maidervierte/epubbold/releases)

## Step 2

Extract the downloaded files anywhere, for example using [7zip](https://www.7-zip.org/).

![2023-08-27 19_51_01-Downloads](https://github.com/Maidervierte/epubbold/assets/68083029/9d96fc0a-bc16-425f-9ae9-5c8c3e4385f5)

## Step 3

Copy the .epub file you want to edit into the input folder (you may remove the example file)

## Step 4

Run the epubbold.exe (Wait for the cmd window to close).

## Step 5

Open the .epub file in the input folder as an archive, for example using [7zip.](https://www.7-zip.org/).

![2023-08-27 19_53_06-input](https://github.com/Maidervierte/epubbold/assets/68083029/b99d5ee6-cbb5-4e58-97bb-bb0e03edf2d2)

## Step 6

Locate the files that make up the content of the ebook. These can be in a different locations depending on the .epub.

In the example they are in /epub/text.

Other examples where they might be:
    - directly in the main folder 
    - /OEBPS/Text
    - directly in /OEBPS/

You can tell you found the correct files by opening them (for example in your browser, as they are x/html files) and seeing the text of your ebook. They are most likely numbered, and each file corresponds to a chapter of the book.

Examples:

![2023-08-27 20_08_18-M__Drive_Python_epub_Epub_input_Hexer_ Das Schwert der Vorsehun - Sapkowski, And](https://github.com/Maidervierte/epubbold/assets/68083029/577d3ae7-3f47-4074-a056-f7211badad45)
![2023-08-27 20_08_04-M__Drive_Python_epub_Epub_input_Metro 2034 - Dmitry Glukhovsky epub_OEBPS_Text_](https://github.com/Maidervierte/epubbold/assets/68083029/6d3a5a19-fc4a-436b-882f-19281f29746b)
![2023-08-27 20_07_51-7-Zip](https://github.com/Maidervierte/epubbold/assets/68083029/b69a4f71-81ba-44fd-a250-1b20207cac0b)
![2023-08-27 20_02_49-M__Drive_Python_epub_Epub_input_Hexer_ Das Schwert der Vorsehun - Sapkowski, And](https://github.com/Maidervierte/epubbold/assets/68083029/b71287dd-6026-4c17-a61e-6e31c76eef70)


## Step 7

Replace the files with the ones from the corresponding output folder.

It may make a mess out of pages with formatting that doesn't fit into how the script reads the files. Since the original isn't altered this isn't critical, worst case scenario should be that you may have to check the messed up pages in the original.

## Step 8 (optional)

Edit the content.opf with a text editor of your choice and change the title. In the example the title can be found on line 29.

![2023-08-27 20_00_46-_content opf - Editor](https://github.com/Maidervierte/epubbold/assets/68083029/8ddcfa26-066f-44e5-8961-fb0ee0139dd6)

## Step 9

Import it to your ebook management program (for example [calibre](https://calibre-ebook.com/)) or put it onto your ereader and check if everything worked.

![2023-08-27 20_51_02-calibre — __ calibre __](https://github.com/Maidervierte/epubbold/assets/68083029/012ca57d-fabc-488e-adbb-d144a5a0a47e)

# Known Bugs

It may make a mess out of pages with formatting that doesn't fit into how the script reads the files. Since the original isn't altered but instead a new copy created this isn't critical and should just be considered and checked during step 7.

There may be some hijinks going on with special characters and accents which may cause words to be bolded incorrectly.





