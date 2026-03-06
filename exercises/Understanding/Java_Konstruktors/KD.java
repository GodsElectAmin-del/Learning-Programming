public class KD {
    String player;
    double kills;
    double deaths;
    double kd;

    public KD(String player, int kills, int deaths){
        this.player = player;
        this.kills = kills;
        this.deaths = deaths;
        this.kd = (double) kills / deaths;
    }
}
