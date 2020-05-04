# IdiotSurf

Text-based web browser for idiots, written by an idiot.

IT IS ONGOING, FAR FROM FINISH
Todo:
- ~prettify with bs4~ done with html2text, why should I need bs4?
- using curses
- 'click' on link
- POST request
- ~history~
- bookmarks

## Tutorial on how to try (I say how to _try_, nobody will use this crap for daily browsing anyway):

1. Make sure you have Python 3 and pip installed.
2. You see 'Clone or download' green button up there? in the right side? Yes, that's it. Click and download zip.
3. Extract and go to that directory
4. Use virtualenv

```python3 -m venv env```

For Linux:

```source env/bin/activate```

For Windows

```env\Scripts\activate.bat```

5. Install requirements

```pip install requirements.txt```

6. Run it

```python3 idiotsurf.py```