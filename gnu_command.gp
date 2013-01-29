set title "Asymmetric V/s Symmetric Encryption "
set xlabel "File size (MB)"
set style data linespoints
set xrange [0.000:1.000]
set yrange [100 : 800]
plot "time_asy.txt" using 1:2 title "Asymmetric" ,  "time_sy.txt" using 1:2 title "Symmetric"

