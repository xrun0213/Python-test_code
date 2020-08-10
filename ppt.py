#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os, pptx
import numpy as np

prs = pptx.Presentation()
title_slide_layout = prs.slide_layouts[0]
slide = prs.slides.add_slide(title_slide_layout)
title = slide.shapes.title
subtitle = slide.placeholders[1]

title.text = "Hello, World!"
subtitle.text = "python-pptx was here! by Tony"

prs.save('output/test.pptx')
