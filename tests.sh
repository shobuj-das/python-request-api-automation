#!/bin/bash

timestamp=$(date +"%Y-%m-%d_%H-%M-%S")

pytest \
-v \
--html="reports/report_$timestamp.html" \
--self-contained-html