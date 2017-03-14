#!/bin/python
#Used to generate a bunch of PBS scripts for forced paralell computing

import sys








def main(*args):
    '''main function'''

    parser = argparse.ArgumentParser(
        description="Generate many PBS scripts for HPC cluster submission")
    parser.add_argument(
        "-v", "--verbose", help="Enable debugging messages to be displayed", action='store_true')
    parser.add_argument(
        "-ko", "--keepOutput", help="Whether or not to keep output", type=str)
    parser.add_argument(
        "-ke", "--keepErrors", help="Whether or not to keep errors", type=str)
    parser.add_argument(
        "-n", "--nodes", help="Number of nodes", type=str)
     parser.add_argument(
        "-p", "--ppn", help="Processors per node", type=str)
     parser.add_argument(
        "-m", "--memory", help="Virtual memory", type=str)
     parser.add_argument(
        "-w", "--walltime", help="Wall time", type=str)
     parser.add_argument(
        "-N", "--notifications", help="String of notifications", type=str)
     parser.add_argument(
        "-na", "--jobName", help="Name for jobs", type=str)
    args = parser.parse_args()
    if args.verbose:
        log.basicConfig(
            format='%(asctime)s %(message)s', datefmt='%m/%d:%I:%M:%S%p', level=log.DEBUG)
    if not args.accession:
        parser.print_help()
        sys.exit(1)
    else:
        queryAN(args.accession)



if __name__ == "__main__":
    main(*sys.argv)




#PBS -k oe #Keep the output and errors from the run
#PBS -l nodes=1:ppn=4,vmem=150gb,walltime=80:00:00
#PBS -M gibsomat@iu.edu
#PBS -m abe # Get notifications for the job
#PBS -N samSortJal

module load samtools

cd /N/dc2/projects/gibsonTomato/jaltomata/rawdata/release_data/bamFiles

ref='/N/dc2/projects/gibsonTomato/genomes/SLA_3.fa'
for f1 in *.bam
do
        #f2=${f1%%_1P.fq}"_2P.fq"
        #echo $f2
        echo $f1
        samtools sort $f1 ../sorted/$f1.sorted

done