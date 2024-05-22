---
title: Dependency Management in Sentry Builds
---
This document will explore how Sentry manages its dependencies during the build process. We'll cover:

1. Overview of Sentry's build configuration
2. Dependency management during the build

<SwmSnippet path="/webpack.config.ts" line="1">

---

# Overview of Sentry's Build Configuration

This file contains the complete build configuration for Sentry using Webpack. It includes definitions for handling different file types, optimizing the build, and configuring development tools. Dependency management is handled through various plugins and loaders that integrate with the build process.

```typescript
/* eslint-env node */

import {WebpackReactSourcemapsPlugin} from '@acemarke/react-prod-sourcemaps';
import {RsdoctorWebpackPlugin} from '@rsdoctor/webpack-plugin';
import browserslist from 'browserslist';
import CompressionPlugin from 'compression-webpack-plugin';
import CopyPlugin from 'copy-webpack-plugin';
import CssMinimizerPlugin from 'css-minimizer-webpack-plugin';
import ForkTsCheckerWebpackPlugin from 'fork-ts-checker-webpack-plugin';
import lightningcss from 'lightningcss';
import MiniCssExtractPlugin from 'mini-css-extract-plugin';
import fs from 'node:fs';
import path from 'node:path';
import TerserPlugin from 'terser-webpack-plugin';
import webpack from 'webpack';
import type {
  Configuration as DevServerConfig,
  ProxyConfigArray,
  Static,
} from 'webpack-dev-server';
import FixStyleOnlyEntriesPlugin from 'webpack-remove-empty-scripts';
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>
