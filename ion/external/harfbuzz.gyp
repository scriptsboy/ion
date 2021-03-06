#
# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
{
  'includes': [
    '../common.gypi',
  ],
  'variables': {
    'hb_src_dir': '<(root_dir)/third_party/harfbuzz',
    'hb_config_dir': '<(root_dir)/third_party/google/harfbuzz',
  },
  'targets': [
    {
      'target_name': 'ionharfbuzz',
      'type': 'static_library',
      'include_dirs': [
        '<(root_dir)',
        '<(hb_src_dir)/src',
        # Allows access to pre-built config.h & hb-version.h.
        '<(hb_config_dir)',
        '<(hb_config_dir)/src',
      ],
      'all_dependent_settings': {
        'include_dirs': [
          '<(root_dir)',
          '<(hb_src_dir)/src',
          # Allows access to pre-built config.h & hb-version.h.
          '<(hb_config_dir)',
          '<(hb_config_dir)/src',
        ],
      },  # all_dependent_settings
      'cflags_cc': [
        '-Wno-conversion',
        '-Wno-null-dereference',
      ],
      'sources': [
        '<(hb_config_dir)/config.h',
        # To generate this list cd into third_party/harfbuzz and run:
        # ls -1 src/*.{h,hh,cc}|egrep -v 'main|test|dump-|hb-(coretext|directwrite|glib|gobject|graphite2|ucdn|uniscribe)'|sed "sI\(.*\)I        '<(hb_src_dir)/\1',I"|LC_ALL=C sort
        '<(hb_src_dir)/src/hb-aat-layout-ankr-table.hh',
        '<(hb_src_dir)/src/hb-aat-layout-common-private.hh',
        '<(hb_src_dir)/src/hb-aat-layout-kerx-table.hh',
        '<(hb_src_dir)/src/hb-aat-layout-morx-table.hh',
        '<(hb_src_dir)/src/hb-aat-layout-private.hh',
        '<(hb_src_dir)/src/hb-aat-layout-trak-table.hh',
        '<(hb_src_dir)/src/hb-aat-layout.cc',
        '<(hb_src_dir)/src/hb-atomic-private.hh',
        '<(hb_src_dir)/src/hb-blob.cc',
        '<(hb_src_dir)/src/hb-blob.h',
        '<(hb_src_dir)/src/hb-buffer-deserialize-json.hh',
        '<(hb_src_dir)/src/hb-buffer-deserialize-text.hh',
        '<(hb_src_dir)/src/hb-buffer-private.hh',
        '<(hb_src_dir)/src/hb-buffer-serialize.cc',
        '<(hb_src_dir)/src/hb-buffer.cc',
        '<(hb_src_dir)/src/hb-buffer.h',
        '<(hb_src_dir)/src/hb-common.cc',
        '<(hb_src_dir)/src/hb-common.h',
        '<(hb_src_dir)/src/hb-debug.hh',
        '<(hb_src_dir)/src/hb-deprecated.h',
        '<(hb_src_dir)/src/hb-dsalgs.hh',
        '<(hb_src_dir)/src/hb-face-private.hh',
        '<(hb_src_dir)/src/hb-face.cc',
        '<(hb_src_dir)/src/hb-face.h',
        '<(hb_src_dir)/src/hb-fallback-shape.cc',
        '<(hb_src_dir)/src/hb-font-private.hh',
        '<(hb_src_dir)/src/hb-font.cc',
        '<(hb_src_dir)/src/hb-font.h',
        '<(hb_src_dir)/src/hb-ft.cc',
        '<(hb_src_dir)/src/hb-ft.h',
        '<(hb_src_dir)/src/hb-icu.cc',
        '<(hb_src_dir)/src/hb-icu.h',
        '<(hb_src_dir)/src/hb-mutex-private.hh',
        '<(hb_src_dir)/src/hb-object-private.hh',
        '<(hb_src_dir)/src/hb-open-file-private.hh',
        '<(hb_src_dir)/src/hb-open-type-private.hh',
        '<(hb_src_dir)/src/hb-ot-cmap-table.hh',
        '<(hb_src_dir)/src/hb-ot-color-cbdt-table.hh',
        '<(hb_src_dir)/src/hb-ot-color-colr-table.hh',
        '<(hb_src_dir)/src/hb-ot-color-cpal-table.hh',
        '<(hb_src_dir)/src/hb-ot-color-sbix-table.hh',
        '<(hb_src_dir)/src/hb-ot-color-svg-table.hh',
        '<(hb_src_dir)/src/hb-ot-color.cc',
        '<(hb_src_dir)/src/hb-ot-font.cc',
        '<(hb_src_dir)/src/hb-ot-font.h',
        '<(hb_src_dir)/src/hb-ot-glyf-table.hh',
        '<(hb_src_dir)/src/hb-ot-hdmx-table.hh',
        '<(hb_src_dir)/src/hb-ot-head-table.hh',
        '<(hb_src_dir)/src/hb-ot-hhea-table.hh',
        '<(hb_src_dir)/src/hb-ot-hmtx-table.hh',
        '<(hb_src_dir)/src/hb-ot-kern-table.hh',
        '<(hb_src_dir)/src/hb-ot-layout-base-table.hh',
        '<(hb_src_dir)/src/hb-ot-layout-common-private.hh',
        '<(hb_src_dir)/src/hb-ot-layout-gdef-table.hh',
        '<(hb_src_dir)/src/hb-ot-layout-gpos-table.hh',
        '<(hb_src_dir)/src/hb-ot-layout-gsub-table.hh',
        '<(hb_src_dir)/src/hb-ot-layout-gsubgpos-private.hh',
        '<(hb_src_dir)/src/hb-ot-layout-jstf-table.hh',
        '<(hb_src_dir)/src/hb-ot-layout-private.hh',
        '<(hb_src_dir)/src/hb-ot-layout.cc',
        '<(hb_src_dir)/src/hb-ot-layout.h',
        '<(hb_src_dir)/src/hb-ot-map-private.hh',
        '<(hb_src_dir)/src/hb-ot-map.cc',
        '<(hb_src_dir)/src/hb-ot-math-table.hh',
        '<(hb_src_dir)/src/hb-ot-math.cc',
        '<(hb_src_dir)/src/hb-ot-math.h',
        '<(hb_src_dir)/src/hb-ot-maxp-table.hh',
        '<(hb_src_dir)/src/hb-ot-name-table.hh',
        '<(hb_src_dir)/src/hb-ot-os2-table.hh',
        '<(hb_src_dir)/src/hb-ot-os2-unicode-ranges.hh',
        '<(hb_src_dir)/src/hb-ot-post-macroman.hh',
        '<(hb_src_dir)/src/hb-ot-post-table.hh',
        '<(hb_src_dir)/src/hb-ot-shape-complex-arabic-fallback.hh',
        '<(hb_src_dir)/src/hb-ot-shape-complex-arabic-private.hh',
        '<(hb_src_dir)/src/hb-ot-shape-complex-arabic-table.hh',
        '<(hb_src_dir)/src/hb-ot-shape-complex-arabic-win1256.hh',
        '<(hb_src_dir)/src/hb-ot-shape-complex-arabic.cc',
        '<(hb_src_dir)/src/hb-ot-shape-complex-default.cc',
        '<(hb_src_dir)/src/hb-ot-shape-complex-hangul.cc',
        '<(hb_src_dir)/src/hb-ot-shape-complex-hebrew.cc',
        '<(hb_src_dir)/src/hb-ot-shape-complex-indic-machine.hh',
        '<(hb_src_dir)/src/hb-ot-shape-complex-indic-private.hh',
        '<(hb_src_dir)/src/hb-ot-shape-complex-indic-table.cc',
        '<(hb_src_dir)/src/hb-ot-shape-complex-indic.cc',
        '<(hb_src_dir)/src/hb-ot-shape-complex-khmer-machine.hh',
        '<(hb_src_dir)/src/hb-ot-shape-complex-khmer-private.hh',
        '<(hb_src_dir)/src/hb-ot-shape-complex-khmer.cc',
        '<(hb_src_dir)/src/hb-ot-shape-complex-myanmar-machine.hh',
        '<(hb_src_dir)/src/hb-ot-shape-complex-myanmar-private.hh',
        '<(hb_src_dir)/src/hb-ot-shape-complex-myanmar.cc',
        '<(hb_src_dir)/src/hb-ot-shape-complex-private.hh',
        '<(hb_src_dir)/src/hb-ot-shape-complex-thai.cc',
        '<(hb_src_dir)/src/hb-ot-shape-complex-tibetan.cc',
        '<(hb_src_dir)/src/hb-ot-shape-complex-use-machine.hh',
        '<(hb_src_dir)/src/hb-ot-shape-complex-use-private.hh',
        '<(hb_src_dir)/src/hb-ot-shape-complex-use-table.cc',
        '<(hb_src_dir)/src/hb-ot-shape-complex-use.cc',
        '<(hb_src_dir)/src/hb-ot-shape-fallback-private.hh',
        '<(hb_src_dir)/src/hb-ot-shape-fallback.cc',
        '<(hb_src_dir)/src/hb-ot-shape-normalize-private.hh',
        '<(hb_src_dir)/src/hb-ot-shape-normalize.cc',
        '<(hb_src_dir)/src/hb-ot-shape-private.hh',
        '<(hb_src_dir)/src/hb-ot-shape.cc',
        '<(hb_src_dir)/src/hb-ot-shape.h',
        '<(hb_src_dir)/src/hb-ot-tag.cc',
        '<(hb_src_dir)/src/hb-ot-tag.h',
        '<(hb_src_dir)/src/hb-ot-var-avar-table.hh',
        '<(hb_src_dir)/src/hb-ot-var-fvar-table.hh',
        '<(hb_src_dir)/src/hb-ot-var-hvar-table.hh',
        '<(hb_src_dir)/src/hb-ot-var-mvar-table.hh',
        '<(hb_src_dir)/src/hb-ot-var.cc',
        '<(hb_src_dir)/src/hb-ot-var.h',
        '<(hb_src_dir)/src/hb-ot.h',
        '<(hb_src_dir)/src/hb-private.hh',
        '<(hb_src_dir)/src/hb-set-digest-private.hh',
        '<(hb_src_dir)/src/hb-set-private.hh',
        '<(hb_src_dir)/src/hb-set.cc',
        '<(hb_src_dir)/src/hb-set.h',
        '<(hb_src_dir)/src/hb-shape-plan-private.hh',
        '<(hb_src_dir)/src/hb-shape-plan.cc',
        '<(hb_src_dir)/src/hb-shape-plan.h',
        '<(hb_src_dir)/src/hb-shape.cc',
        '<(hb_src_dir)/src/hb-shape.h',
        '<(hb_src_dir)/src/hb-shaper-impl-private.hh',
        '<(hb_src_dir)/src/hb-shaper-list.hh',
        '<(hb_src_dir)/src/hb-shaper-private.hh',
        '<(hb_src_dir)/src/hb-shaper.cc',
        '<(hb_src_dir)/src/hb-string-array.hh',
        '<(hb_src_dir)/src/hb-subset-glyf.cc',
        '<(hb_src_dir)/src/hb-subset-glyf.hh',
        '<(hb_src_dir)/src/hb-subset-input.cc',
        '<(hb_src_dir)/src/hb-subset-plan.cc',
        '<(hb_src_dir)/src/hb-subset-plan.hh',
        '<(hb_src_dir)/src/hb-subset-private.hh',
        '<(hb_src_dir)/src/hb-subset.cc',
        '<(hb_src_dir)/src/hb-subset.h',
        '<(hb_src_dir)/src/hb-unicode-private.hh',
        '<(hb_src_dir)/src/hb-unicode.cc',
        '<(hb_src_dir)/src/hb-unicode.h',
        '<(hb_src_dir)/src/hb-utf-private.hh',
        '<(hb_src_dir)/src/hb-version.h',
        '<(hb_src_dir)/src/hb-warning.cc',
        '<(hb_src_dir)/src/hb.h',
      ],  # sources
      'dependencies': [
        'freetype2.gyp:ionfreetype2',
        'icu.gyp:ionicu',
      ],
      'conditions': [
        ['OS == "win"', {
          'msvs_disabled_warnings': [
            4005, # Macro redefinition (WIN32_LEAN_AND_MEAN on cmdline).
            4244, # Conversion from 'x' to 'y', possible loss of data.
            4267, # Conversion from 'x' to 'y', possible loss of data.
            4334, # Result of 32-bit shift implicitly converted to 64 bits.
            4996, # 'strdup': POSIX name is deprecated.
          ],
          'defines' : [
            'ALIGNOF_STRUCT_CHAR__=1',
            'HAVE_ATEXIT=1',
            'HAVE_DLFCN_H=1',
            'HAVE_FALLBACK=1',
            'HAVE_FREETYPE=1',
            'HAVE_FT_FACE_GETCHARVARIANTINDEX=1',
            'HAVE_GETPAGESIZE=1',
            'HAVE_ICU=1',
            'HAVE_INTEL_ATOMIC_PRIMITIVES=1',
            'HAVE_INTTYPES_H=1',
            'HAVE_ISATTY=1',
            'HAVE_MEMORY_H=1',
            'HAVE_MMAP=1',
            'HAVE_MPROTECT=1',
            'HAVE_OT=1',
            'HAVE_PTHREAD=1',
            'HAVE_STDINT_H=1',
            'HAVE_STDLIB_H=1',
            'HAVE_STRINGS_H=1',
            'HAVE_STRING_H=1',
            'HAVE_SYSCONF=1',
            'HAVE_SYS_STAT_H=1',
            'HAVE_SYS_TYPES_H=1',
            'HB_NO_UNICODE_FUNCS=1',
            'LT_OBJDIR=".libs/"',
            'PACKAGE_BUGREPORT="http://bugs.freedesktop.org/enter_bug.cgi?product=harfbuzz"',
            'PACKAGE_NAME="HarfBuzz"',
            'PACKAGE_STRING="HarfBuzz 0.9.33"',
            'PACKAGE_TARNAME="harfbuzz"',
            'PACKAGE_URL="http://harfbuzz.org/"',
            'PACKAGE_VERSION="0.9.33"',
            'STDC_HEADERS=1',
          ],
        },
        {
          'defines': [
            'HAVE_CONFIG_H',
            '__ion__',
          ],
        }],
      ],
    },  # target: ionharfbuzz
  ],  # targets
}
