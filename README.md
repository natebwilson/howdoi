# HOW DO I...

Simple CLI command built in Python to make using Linux a little easier.

Biggest issue is the prompt kind of sucks and often overcomplicates things. For example, executing  
```howdoi get number of lines of code in current directory```  
will often return something like  
```find . -type f -name "*.c" -o -name "*.cpp" -o -name "*.h" | xargs wc -l```  
which:  
1. Hallucinates additional details (I did not specify what language I was coding in)
2. Is an overwrought command. It could simply return ```ls | xargs wc -l```.
