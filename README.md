# Meteor

Meteor was first designed to help you learn Chinese language, but it appear that you could do a lot more things. It's a very simple, very minimalist learning tool for everything that can be hand writen and displayed on a screen. Language, Mathematics formula, Family birthday, you can learn whatever you want.

## Last Released Version

* For Windows: 
    * (pre-release) [Language Training v0.2](https://github.com/Vikka/Meteor/releases/download/v0.2/language_training_v0.2.zip)
* For Macintosh:
    * Not yet released
* For Linux:
    * Not yet released

## How to use it

Work In Progress

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