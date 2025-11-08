---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Slurm

Slurm is a cluster management system that allows users to manage and schedule jobs on a cluster of computers. A Together GPU Cluster provides Slurm configured out-of-the-box for distributed training and the option to use your own scheduler. Users can submit computing jobs to the Slurm head node where the scheduler will assign the tasks to available GPU nodes based on resource availability. For more information on Slurm, see the [Slurm Quick Start User Guide](https://slurm.schedmd.com/quickstart.html).

### **Slurm Basic Concepts**

1. **Jobs**: A job is a unit of work that is submitted to the cluster. Jobs can be scripts, programs, or other types of tasks.
2. **Nodes**: A node is a computer in the cluster that can run jobs. Nodes can be physical machines or virtual machines.
3. **Head Node**: Each Together GPU Cluster cluster is configured with head node. A user will login to the head node to write jobs, submit jobs to the GPU cluster, and retrieve the results.
4. **Partitions**: A partition is a group of nodes that can be used to run jobs. Partitions can be configured to have different properties, such as the number of nodes and the amount of memory available.
5. **Priorities**: Priorities are used to determine which jobs should be run first. Jobs with higher priorities are given preference over jobs with lower priorities.

### **Using Slurm**

1. **Job Submission**: Jobs can be submitted to the cluster using the **`sbatch`** command. Jobs can be submitted in batch mode or interactively using the **`srun`** command.
2. **Job Monitoring**: Jobs can be monitored using the **`squeue`** command, which displays information about the jobs that are currently running or waiting to run.
3. **Job Control**: Jobs can be controlled using the **`scancel`** command, which allows users to cancel or interrupt jobs that are running.

### Slurm Job Arrays

You can use Slurm job arrays to partition input files into k chunks and distribute the chunks across the nodes. See this example on processing RPv1 which will need to be adapted to your processing: [arxiv-clean-slurm.batch](https://github.com/togethercomputer/RedPajama-Data/blob/rp_v1/data_prep/arxiv/scripts/arxiv-clean-slurm.sbatch)

### **Troubleshooting Slurm**

1. **Error Messages**: Slurm provides error messages that can help users diagnose and troubleshoot problems.
2. **Log Files**: Slurm provides log files that can be used to monitor the status of the cluster and diagnose problems.


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
