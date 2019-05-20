# Meteor

Meteor was first designed to help you learn Chinese language, but it appear that you could do a lot more things. It's a very simple, very minimalist learning tool for everything that can be hand writen and displayed on a screen. Language, Mathematics formula, Family birthday, you can learn whatever you want.

## Last Released Version

* For Windows: 
    * (pre-release) [Language Training v0.1.1](https://github.com/Vikka/Meteor/releases/download/v0.1.1/language_training_v0.1.1.zip)
* For Macintosh:
    * Not yet released
* For Linux:
    * Not yet released

## How to use it

Meteor allow you to select multiple sets of elements.

First step, select one or more :

![main_window of Meteor](https://user-images.githubusercontent.com/9381120/47983500-73006e80-e10e-11e8-89c7-e29fbd93ba2a.PNG)

Then, the first element will be displayed, the only thing you have to do is write (or "think" for lazy) the corresponding asked answer.

![main_window of Meteor](https://user-images.githubusercontent.com/9381120/47984022-40f00c00-e110-11e8-9f76-adb7ac844770.PNG)

Then, press `Show Solution` button.

![main_window of Meteor](https://user-images.githubusercontent.com/9381120/47984744-80b7f300-e112-11e8-9960-f99f8dbbc042.PNG)

If your answers is correct compared to the solution, select `Correct` and the word will appears less often, if not, select `False` and the word will appear more often.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You need to install [Python 3.6](https://www.python.org/downloads/) or later.

If you are on Ubuntu, it comes with both python 2.7 and python 3.5. It's recommended to install and use Python 3.6 instead.

You need to install [PyInstaller](https://pyinstaller.readthedocs.io/en/stable/) if you want to compile it.

### Compiling

Use `pyinstaller` in order to compile everything in a `.exe`. 

```
pyinstaller ./chi_train.py
```

If you want to compile for production, use `-w` option in order to hide the console.
```
pyinstaller -w ./chi_train.py
```

You must copy a default file named `sets.json` in a folder named `sets`.

```
mkdir ./dist/chi_train/sets
cp ./sets/sets.json ./dist/chi_train/sets
```

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the tags on this repository.

## Authors

* **Dorian Turba** - *Initial work* - [Vikka](https://github.com/Vikka)

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details
