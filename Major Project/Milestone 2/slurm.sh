#!/bin/bash -l
#SBATCH --job-name=CudaGoL
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=4G
#SBATCH --partition=gpu
#SBATCH --gres=gpu:1
#SBATCH --time=0-01:00 # time (D-HH:MM)
#SBATCH --constraint=R740

export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK}
export MKL_NUM_THREADS=${SLURM_CPUS_PER_TASK}
echo 'running with OMP_NUM_THREADS =' $OMP_NUM_THREADS
echo 'running with MKL_NUM_THREADS =' $MKL_NUM_THREADS
echo "This is job '$SLURM_JOB_NAME' (id: $SLURM_JOB_ID) running on the following nodes:"
echo $SLURM_NODELIST
echo "running with OMP_NUM_THREADS= $OMP_NUM_THREADS "
echo "running with SLURM_TASKS_PER_NODE= $SLURM_TASKS_PER_NODE "

module load cuda/10.0 gnu/7.2.0

make

for o in {0..3}
do
    for m in {20..20}
    do
        for i in {1..20}
        do
            nvprof ./cudaCellular$(($o)) $((50*$i)) $((50*$m)) >> results_O$(($o)).out
        done
    done
done

echo 'FINISHED'