# Copy Block Builder

This project, while initially developed to build my cover letters for job hunting, can be used to build any sort of canned responses that you would need with variable content.

```
copy-block-builder
├── README.md
├── requirements.txt
├── coverlettermajig.py
├── data
|   ├── __init__.py
|   ├── data.py         // Not setup yet
|   └── content 
|       ├── closing.txt // The closing paragraphs and signature
|       ├── des.txt     // UI and Brand Design specific content
|       ├── dev.txt     // Developer specific content
|       ├── intro.txt   // Introduction paragraph including customizable valprop
|       └── uxd.txt     // UX Design specific content
└── tests
    └── ...
```

## Installation & Usage

1. Download
2. Adjust the content to your needing
    - Replace or modify any of the files within the `./data/content` directory
    - Update the `./data/map.json` file to suit your needs (see "Updating Content")
3. Run in terminal with `$ python coverlettermajig.py`
    - The terminal will ask a series of questions and build the cover letter
    - Output prints in the terminal for now

> NOTE: The "intro" content block should include the following tokens in order to function properly
> - `{{ salutation }}`: The name of the person you are contacting (defaults to "hiring manager")
> - `{{ position }}`: The position you are applying to
> - `{{ company }}`: The company you are applying to
> - `{{ valprop }}`: Your valprop (which can be updated in `coverlettermajig.py` for now. This allows you to use a standard valprop or change it to a custom one if you feel the cover letter requires that.)


TODO: Output to an easier space for copying/pasting, and consider output to file. 

**Requires Python 3.7+**

## Updating Content

The `./data/map.json` file houses all of the information you will need to change in order to get the prompt questions 
as well as copy blocks updated.

### Example File
```json
{
  "uxd": {
    "question": "Is this a UX focused job?",
    "answer": false,
    "file": "content_experiencedesign.txt"
  },
  "dev": {
    "question": "Is this a development focused job?",
    "answer": false,
    "file": "content_development.txt"
  },
  "design": {
    "question": "Is this a design focused job?",
    "answer": false,
    "file": "content_design.txt"
  }
}
```

You can update the keys (`uxd`, `dev`, `design`) for each node to be whatever makes sense for you. They are not hard-coded into the application 
and are for your reference only.

The `question` is the prompt that will be displayed in the command line. All questions default to `false` and if you do not enter "y" or "yes", the block will be ignored.

If you choose "yes", you will need to make sure the file exists in the directory and the name has been updated in the mapping.

You do not need to include the directory structure, all content must be placed within `./data/content` and be formatted as a `.txt` file to work.

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D
