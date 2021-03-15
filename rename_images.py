import os 
import argparse
from os import listdir

# Function to rename multiple files 
def main(input_dir,output_dir): 
	listing = listdir(input_dir)
	print(input_dir)
	print(listing)
	for count,filename in enumerate(listing): 
		print(count)
		print(filename)
		dst ="image" + str(count) + ".jpg"
		src =args.input_dir+'/'+ filename 
		print(src)
		dst =args.output_dir+'/'+ dst 
		os.rename(src, dst) 

def parse_args():
    parser = argparse.ArgumentParser(description="path of input and output dir for conversion")
    parser.add_argument(
        '--input_dir',
        '-i',
        help='name of input dir where original images are present for renaming',
        default=" ",
        # required=True
    )
    parser.add_argument(
        '--output_dir',
        '-o',
        help="path of output directory where rename images will save",
        default=" ",
        # required=True

    )
    return parser.parse_args()
# Driver Code 
if __name__ == '__main__': 
	args = parse_args()
	main(args.input_dir, args.output_dir)
	# main() 

