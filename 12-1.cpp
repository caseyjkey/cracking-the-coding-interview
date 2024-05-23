// Write a function to output the last K lines of a file


#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

int main(int argc, char *argv[]) {
	int numLines = atoi(argv[1]);
	cout << "Outputting last " << numLines << " lines." << endl;
	string filename = "12-1.txt";
	ifstream fin;
	fin.open(filename);
	if (fin.is_open()) {
		fin.seekg(-2, ios_base::end);

		bool keepLooping = true;
		int lines = 0;
		while (keepLooping) {
			char ch;
			fin.get(ch);
			if ((int)fin.tellg() <= 1) {
				fin.seekg(0);
				keepLooping = false;
			}
			else if (ch == '\n') {
				lines += 1;
				keepLooping = lines < numLines;
				fin.seekg(-2, ios_base::cur);
			}
			else {
				fin.seekg(-2, ios_base::cur);
			}
		}

		string lastLine;
		for (int i = 0; i < numLines; i++) {
			getline(fin, lastLine);
			cout << "Result: " << lastLine << '\n';
		}

		fin.close();

	}

	return 0;
}
