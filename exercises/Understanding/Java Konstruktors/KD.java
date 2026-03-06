public class KD {
    String player;
    double kills;
    double deaths;

    public KD(String player, int kills, int deaths){
        this.player = player;
        this.kills = kills;
        this.deaths = deaths;
        double kd = kills / deaths;
    }
}
