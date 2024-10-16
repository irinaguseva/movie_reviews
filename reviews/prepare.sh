#!/bin/bash

gunzip -c aclImdb_v1.tar.gz | tar xopf -

cd aclImdb

mkdir movie_data

for split in train test;
do

  for sentiment in pos neg;
  do 
    
    for file in $split/$sentiment/*; 
    do
              cat $file >> movie_data/full_${split}.txt; 
              echo >> movie_data/full_${split}.txt; 

    done;
  done;
done;