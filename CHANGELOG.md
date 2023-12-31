# Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)

## [0.1.4]

### Fixed

- An issue where the database output path was printed as `None`

## [0.1.3]

### Added

- Support for `--no-owner` flag to ignore role on import and backup

## [0.1.2]

### Changed

- Dropped binary psycopg2

## [0.1.1]

### Fixed

- Dropped exitstatus from requirements

## [0.1.0]

# Added

- Keep only the latest 5 backups for each database name
- Reminder to add backup destination to backup operation

### Changed

- Unix time stamp in filename is now in seconds (was milliseconds)

## [0.0.2]

### Added

- Restore operation
- List operation

## [0.0.1]

### Fixed

- Initial release
