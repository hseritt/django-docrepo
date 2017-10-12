#!/usr/bin/env bash

pylint 	--rcfile=pylintrc \
		--ignore-patterns=migrations \
		--load-plugins pylint_django \
		apps docrepo \
	   
