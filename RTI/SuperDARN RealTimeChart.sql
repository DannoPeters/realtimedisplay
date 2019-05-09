CREATE TABLE `RADAR`
(
  `station_id` varchar(255) PRIMARY KEY
);

CREATE TABLE `beam_data`
(
  `station_id` varchar(255),
  `beam_num` int,
  `time_UTC` datetime,
  `range_gate` int,
  `program` varchar(255),
  `program_id` int,
  `freq` int,
  `velocity` varbinary,
  `snr` varbinary,
  `spectral_width` varbinary,
  `elevation` varbinary
);

ALTER TABLE `beam_data` ADD FOREIGN KEY (`station_id`) REFERENCES `RADAR` (`station_id`);
