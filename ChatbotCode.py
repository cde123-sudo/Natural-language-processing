{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ebb2c1c8-25ca-4f35-95a5-ce15c9fd2b1e",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[nltk_data] Downloading package punkt to\n",
      "[nltk_data]     C:\\Users\\m9nsu\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]   Package punkt is already up-to-date!\n",
      "[nltk_data] Downloading package stopwords to\n",
      "[nltk_data]     C:\\Users\\m9nsu\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]   Package stopwords is already up-to-date!\n",
      "[nltk_data] Downloading package averaged_perceptron_tagger to\n",
      "[nltk_data]     C:\\Users\\m9nsu\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]   Package averaged_perceptron_tagger is already up-to-\n",
      "[nltk_data]       date!\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "==================================================\n",
      "  Welcome to Student Academic Assistant Chatbot\n",
      "==================================================\n",
      "  Type 'bye' to exit\n",
      "\n"
     ]
    }
   ],
   "source": [
    "import nltk\n",
    "from nltk.tokenize import word_tokenize\n",
    "from nltk.corpus import stopwords\n",
    "from nltk import pos_tag\n",
    "\n",
    "nltk.download('punkt')\n",
    "nltk.download('stopwords')\n",
    "nltk.download('averaged_perceptron_tagger')\n",
    "\n",
    "def preprocess(text):\n",
    "    tokens = word_tokenize(text.lower())\n",
    "    stop_words = set(stopwords.words('english'))\n",
    "    filtered = [w for w in tokens if w not in stop_words]\n",
    "    return filtered\n",
    "\n",
    "def chatbot():\n",
    "    print(\"=\" * 50)\n",
    "    print(\"  Welcome to Student Academic Assistant Chatbot\")\n",
    "    print(\"=\" * 50)\n",
    "    print(\"  Type 'bye' to exit\\n\")\n",
    "\n",
    "    while True:\n",
    "        user_input = input(\"You: \")\n",
    "        tokens = preprocess(user_input)\n",
    "\n",
    "        if any(word in user_input.lower() for word in [\"hello\", \"hi\", \"hey\", \"good morning\", \"good afternoon\"]):\n",
    "            print(\"Bot: Hello! Welcome to the Student Academic Assistant. How can I help you today?\\n\")\n",
    "\n",
    "        elif any(word in user_input.lower() for word in [\"cat\", \"exam\", \"test\", \"assessment\", \"schedule\", \"when\"]):\n",
    "            print(\"Bot: CAT 1 is scheduled for next week and will cover all topics from Week 1 to Week 5.\")\n",
    "            print(\"     Topics include tokenization, POS tagging, N-grams, HMMs, parsing and semantic analysis.\\n\")\n",
    "\n",
    "        elif any(word in user_input.lower() for word in [\"register\", \"registration\", \"unit\", \"enroll\", \"course\", \"subject\"]):\n",
    "            print(\"Bot: For unit registration please visit the student portal at your university website.\")\n",
    "            print(\"     Registration for next semester opens at the end of this month.\\n\")\n",
    "\n",
    "        elif any(word in user_input.lower() for word in [\"nlp\", \"tokenize\", \"pos\", \"ngram\", \"parsing\", \"semantic\"]):\n",
    "            print(\"Bot: NLP stands for Natural Language Processing. This unit covers tokenization,\")\n",
    "            print(\"     POS tagging, N-grams, Hidden Markov Models, dependency parsing and semantic similarity.\\n\")\n",
    "\n",
    "        elif \"help\" in user_input.lower():\n",
    "            print(\"Bot: I can help you with:\")\n",
    "            print(\"     1. CAT and exam schedules\")\n",
    "            print(\"     2. Unit registration information\")\n",
    "            print(\"     3. NLP topic questions\")\n",
    "            print(\"     Type any of these topics to get started.\\n\")\n",
    "\n",
    "        \n",
    "        elif any(word in user_input.lower() for word in [\"bye\", \"goodbye\", \"exit\", \"quit\"]):\n",
    "            print(\"Bot: Goodbye! Good luck with your studies. All the best for CAT 1!\\n\")\n",
    "            break\n",
    "\n",
    "        else:\n",
    "            print(\"Bot: I'm sorry I did not understand that. Type 'help' to see what I can assist with.\\n\")\n",
    "\n",
    "chatbot()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
