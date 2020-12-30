# OpenTX en Esperanto

Tiu ĉi deponejo entenas voĉajn registraĵojn por radiotranssendiloj kongruaj kun [OpenTX](https://github.com/opentx/opentx).

## Instalo

La mikroprogramaro de OpenTX ne konsideras Esperanton inter siaj ekipitaj lingvoj. Tial, se vi volas voĉon en Esperanto sur via radiotranssendilo, estas necese, ke vi kopiu la dosierojn de tiu ĉi deponejo en ```SOUNDS/en``` kaj anstataŭigu ĝian entenon.

## Programado

Se vi volas aldoni aŭ ĝisdatigi la tradukojn, estas necese modifi la dosieron ```SOUNDS/en/SYSTEM/eo-EO-taranis.csv``` kaj poste ruli ```python3 tts_eo.py```. Tio generos la novajn sondosierojn. Tamen antaŭ ol fari tion, instalu ```sox``` tajpante ```sudo apt-get install sox libsox-fmt-mp3```.

La voĉoj en Esperanto estas produktitaj danke al [Parol](https://parol.martinrue.com/), projekto kreita de [Martin Rue](https://github.com/martinrue).

## Traduko

Miaj tradukoj baziĝas sur la jenaj rimedoj:
* [Vikipedio](https://eo.wikipedia.org)
* [Glosbe](https://glosbe.com/en/eo/)
* [Komputeko](https://komputeko.net/)
* Aeronaŭtika Terminaro (E. D. Durrant)

Tamen multaj specifaj vortoj uzataj en dinamika modelismo ofte ne havas rektan tradukon en Esperanto kaj nenie troveblas kolekto pri la leksikono uzata en tiu ĉi fako. Tial mi volus uzi tiun ĉi deponejon ankaŭ kiel vortaron pri dinamika modelismo en Esperanto. Gxia enteno estas legebla sube. Se vi volas aldoni novajn vortojn aŭ proponi aliajn tradukojn, vi povas krei atentindaĵon (*issue*) por diskuti tie aŭ sendi tirpeton (*pull request*).

| Angla                                              | Esperanto                                          |
| -------------------------------------------------- | -------------------------------------------------- |
| Drone                                              | Droneo, flugroboto                                 |
| - Unmanned Aerial Vehicle (UAV)                    | Senpilota aviadilo (spavo)                         |
| - Racing drone                                     | Vetkura droneo                                     |
| - Freestyle drone                                  | Liberstila droneo                                  |
| - Long range drone                                 | Longdistanca droneo                                |
| - Quadcopter, quadrotor, quad                      | Kvarkoptero, kvarrotoro, kvaro                     |
| Frame                                              | Kadro                                              |
| - Carbon fiber                                     | Karbonfibro                                        |
| Motor                                              | Motoro                                             |
| - Brushed motor                                    | Brosa motoro                                       |
| - Brushless motor                                  | Senbrosa motoro                                    |
| - Shaft                                            | Ŝafto                                              |
| Flight controller                                  | Flugregilo                                         |
| Electronic Speed Controller (ESC)                  | Elektronika rapidregilo                            |
| Battery Eliminator Circuit (BEC)                   | Bateriforiganta cirkvito                           |
| Props                                              | Helicoj                                            |
| Battery                                            | Baterio                                            |
| - Lithium-polymer battery                          | Litia-polimera akumulatoro                         |
| - Lithium-ion battery                              | Litia-jona akumulatoro                             |
| - Lithium-iron-phosphate battery                   | Litia-fera-fosfata akumulatoro                     |
| - Nickel-cadmium battery                           | Nikelo-kadmia akumulatoro                          |
| - Nickel-metal hydride battery                     | Nikelo-metalohidrida akumulatoro                   |
| - Battery charger                                  | Bateria ŝargilo                                    |
| - Voltage                                          | Tensio                                             |
| - Current                                          | Kurento                                            |
| - Power                                            | Povumo                                             |
| - Cell                                             | Ĉelo                                               |
| Camera                                             | Kamerao                                            |
| - Camera tilt                                      | Kameraa dekliveco                                  |
| - Field of view                                    | Vidkampo                                           |
| Antenna                                            | Anteno                                             |
| Video transmitter                                  | Videotranssendilo                                  |
| Buzzer                                             | Zumilo                                             |
| Transponder                                        | Transsendrespondilo                                |
| Gyroscope                                          | Giroskopo                                          |
| Accelerometer                                      | Akcelometro                                        |
| Barometer                                          | Barometro                                          |
| Variometer                                         | Variometro                                         |
| Magnetometer                                       | Magnetometro                                       |
| Goggles                                            | Vidilo                                             |
| On-Screen Display (OSD)                            | Surekrana videbligo                                |
| Radio transmitter                                  | Radiotranssendilo                                  |
| Receiver                                           | Ricevilo                                           |
| - Diversity receiver                               | Diverseca ricevilo                                 |
| Radio-controlled (RC)                              | Radioregata                                        |
| Radio-controller                                   | Radioregilo                                        |
| (Frequency) band                                   | (Frekvenc)bendo                                    |
| Channel                                            | Kanalo                                             |
| Telemetry                                          | Telemetrio                                         |
| Failsafe                                           | Panetolera, panetoleremo                           |
| Flyaway                                            | Forflugo                                           |
| Bind                                               | Bindi                                              |
| Bando                                              | Forlasejo                                          |
| Stick                                              | Stango                                             |
| Switch                                             | Ŝaltilo                                            |
| Servo-                                             | Relajso-                                           |
| Trim                                               | Kompensilo                                         |
| Timer                                              | Tempomezurilo                                      |
| Gimbal                                             | Kardano                                            |
| Throttle                                           | Gaso                                               |
| Roll                                               | Ruliĝo                                             |
| Pitch                                              | Tango                                              |
| Yaw                                                | Joro                                               |
| Payload                                            | Utila ŝarĝo                                        |
| Thrust                                             | Puŝo, tiro                                         |
| Ground effect                                      | Grundefiko                                         |
| Flap                                               | Flapo, postklapo                                   |
| Spoiler                                            | Defleksilo                                         |
| Crow                                               | Birdobremso                                        |
| Armed, disarmed                                    | Armita, malarmita                                  |
| Flight mode                                        | Flugreĝimo                                         |
| - Acro                                             | Akrobata                                           |
| - Angle                                            | Angula                                             |
| - Horizon                                          | Horizonta                                          |
| - Manual                                           | Mana                                               |
| - Stabilized                                       | Stabiligita                                        |
| - Head-less                                        | Senkapa                                            |
| Air mode                                           | Aera reĝimo                                        |
| Rate                                               | Angulrapido                                        |
| Resistor                                           | Rezistanco                                         |
| Capacitor                                          | Kondensatoro                                       |
| Inductor                                           | Induktilo, bobeno                                  |
| Ground (electronics)                               | Tero                                               |
| Firmware                                           | Mikroprogramaro                                    |
| Altitude                                           | Altitudo                                           |
| Pilot                                              | Piloto                                             |
| Flight                                             | Flugo                                              |
| - Take off                                         | Ekflugi                                            |
| - Land                                             | Alteriĝi                                           |
| - Hover                                            | Sxvebi                                             |
| - Drift                                            | Drivi                                              |
| - Turn                                             | Turni                                              |
| - Spin                                             | Spirali                                            |
| - Axial roll                                       | Aksa ruliĝo                                        |
| - Yaw spin                                         | Jora spiralo                                       |
| - Crash                                            | Kraŝi                                              |
| Race elements                                      | Konkursaj elementoj                                |
| - Gate                                             | Pasejo                                             |
| - Flag                                             | Flago                                              |
| - Slalom                                           | Slalomo                                            |
| - Carousel                                         | Karuselo                                           |
| - Tunnel                                           | Tunelo                                             |
| - Ladder                                           | Ŝtupetaro                                          |
| - Hurdle                                           | Obstaklo                                           |
| - Corkscrew                                        | Korktirilo                                         |
| - Powerloop                                        | Povlopo                                            |
| - Climbing                                         | Grimpado                                           |
| - Dive                                             | Plonĝo                                             |
