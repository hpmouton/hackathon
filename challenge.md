Hackathon Challenge
===================

The challenge for this hackathon uses a dataset from a mobile telecommunication company [MTC](https://www.mtc.com.na/). It contains information about subscriber activity during the year 2019. Each sample in the dataset contains a **date**, a subscriber **number** and the **status** of the subscriber's number on that date. The example below shows a few records of subscriber status on January 1st 2019.

```json
{
	"date": "20190101",
	"user": "301727881",
	"sdp_status": "active"
},
{
	"date": "20190101",
	"user": "573750881901",
	"sdp_status": "active"
},
{
	"date": "20190101",
	"user": "6475155981",
	"sdp_status": "installed_preactive"
}
```
The subscriber status follows a lifecycle depicted in the diagram below.

![status lifecycle](../images/user-status-lifecycle_indabax-hackathon.png)

The dataset comprises similar records for 352 days, with a set of subscriber status observations per day. For convenience (to upload/download), we grouped the files in a tarball per month. Note that to access the data, you will need [Git LFS](https://git-lfs.github.com/), a tool that helps manage large file storage with git.

# Problem
Your task for this hackathon is to answer the questions below:

1. Predict the values of the missing days;
1. Predict the growth for the year 2020;
1. Identify what the most extended period a customer has been **active** consecutively is;
1. Identify the likelihood for a user to reactivate an expired number (**expired** to **active**) vs cancelling it (**expired** to **cutoff**).
