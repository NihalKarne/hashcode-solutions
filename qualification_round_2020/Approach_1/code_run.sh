#!/bin/sh

input_folder="./input"
output_folder="./output"
files=(a_example
       b_read_on
       c_incunabula
       d_tough_choices
       e_so_many_books
       f_libraries_of_the_world)

for i in "${files[@]}";
do
#  echo "$folder"/"$i".txt
   python3 main.py < "$input_folder"/"$i".txt > "$output_folder"/"$i"_output.txt
done