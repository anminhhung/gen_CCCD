# create output dir
if [ ! -d "$gen_text_results" ]; then
  mkdir gen_text_results
fi

# Gendata
for value in GiaTriDen GioiTinh HoTen NgayThangSinh NoiThuongTru QueQuan QuocTich 
do
    python3 trdg/run.py -c 5 -w 1 -f 40 -l vi -b --dict dictionary/$value.txt --image_dir crop_images/$value --output_dir gen_text_results/$value
done

# gen so
python3 trdg/run.py -c 5 -w 1 -f 40 -l vi -b --dict dictionary/So.txt --image_dir crop_images/So --output_dir gen_text_results/So --text_color '#ff0000,#e50000'